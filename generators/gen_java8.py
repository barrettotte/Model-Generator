import warnings
import utils as utils
from .model import Model,Property

class gen_java8:

    def __init__(self, config, lang_config):
        self.project_pkg = lang_config["namespace"]
        self.annotation_config = None
        if "annotation" in lang_config.keys():
            self.annotation_config = lang_config["annotation"]

    # Parse schema and build model
    def generate(self, schema, obj_path):
        model = Model(obj_path[-1], '/'.join(obj_path)+'.json')
        model.namespace = self.bld_namespace(obj_path)
        model.inheritance = self.bld_inheritance(schema)
        model.imports = self.bld_imports(model.inheritance, obj_path)
        
        annotations,imports = self.bld_annotations()
        model.annotations = annotations
        if len(imports) > 0: 
            model.imports.append('')
            model.imports += imports
        
        props,imports = self.bld_props(schema)
        model.properties = props
        if len(imports) > 0:
            model.imports.append('')
            model.imports += imports
        return model

    # Replace file references with classes and inject additional imports
    def inject_models(self, model, models_dict):
        targets = []
        for prop in model.properties:
            if ".json" in prop.kind: 
                target = self.get_json_ref(prop.kind)
                targets.append(target)
                prop.kind = prop.kind.replace(target, target.split('/')[-1][:-5])
        for imp in self.bld_imports(targets, model.ref):
            model.imports.insert(0,imp[:-5])
        return model
    
    # Get model reference within collection -> ex:  "List<Common/Thing.json>" = "Common/Thing.json"
    def get_json_ref(self, s):
        return s[s.rfind('<')+1:s.find('>')] if ('<' in s) else s

    # Generate source code from model
    def make_code(self, model):
        lines = ["package " + model.namespace + ";\n"]
        for imp in model.imports:
            lines.append(("import " + imp + ";") if (len(imp) > 0) else '')
        lines.append('\n' + '\n'.join(model.annotations))
        lines.append(self.bld_class_dec(model) + '\n')

        for p in model.properties:
            lines.append("    " + p.access + " " + p.kind + " " + p.identifier + ";")
        lines.append(self.bld_dft_ctor(model))

        for p in model.properties:
            lines.append(self.bld_prop_methods(p))
        lines.append("}")
        return '\n'.join(lines)

    # Build default constructor
    def bld_dft_ctor(self, model):
        lines = []
        lines.append("public " + model.identifier + "() {")
        for p in model.properties:
            init = self.init_prop(p)
            if len(init) > 0: lines.append("    this." + init + ";")
        lines.append("}")
        return "\n    " + "\n    ".join(lines)

    # Get suffix for literal value if needed
    def get_suffix(self, kind):
        k = kind.lower()
        if k == "long":     return "L"
        if k == "double":   return "D"
        if k == "float":    return "F"
        return ''

    # Set default value for property
    def prop_dft(self, prop):
        dft = str(prop.default)
        if prop.kind == "String": 
            dft = "\"" + prop.default + "\""
        return prop.identifier + " = " + dft + self.get_suffix(prop.kind)
    
    # Default params for new obj -> ex: this.bd = new BigDecimal(0)
    def init_obj(self, prop):
        kind = self.collection_impl(prop.kind)
        obj_suffix = "()"
        if kind == "BigDecimal": obj_suffix = "(0)"
        return prop.identifier + " = new " + kind + obj_suffix

    # Implement collection interfaces
    def collection_impl(self, kind):
        impl = kind
        if "List<" in kind:  impl = impl.replace("List<","ArrayList<")
        if "Map<"  in kind:  impl = impl.replace("Map<","HashMap<")
        if "Set<"  in kind:  impl = impl.replace("Set<","HashSet<")
        return impl
    
    # Initialize array -> ex: myArr = new String[]
    def init_arr(self, prop):
        if prop.max_items:
            kind = prop.kind.replace("[]", "[" + str(prop.max_items) + "]")
            return prop.identifier + " = new " + kind
        raise Exception("Cannot initialize primitive array '" + str(prop) + "' without 'maxItems' declared.")

    # Build property initialize statement -> ex: this.arr = new String[10];
    def init_prop(self, prop):
        if prop.default:
            return self.prop_dft(prop)
        if "[]" in prop.kind:
            return self.init_arr(prop)
        if self.is_complex_type(prop.kind):
            return self.init_obj(prop)
        return ''

    # Check if type is not a primitive value
    def is_complex_type(self, kind):
        return not kind in [
            "String","Integer","int","Double","double","Boolean","boolean",
            "Float","float","Byte","byte","short","Short","long","Long"]

    # Build annotations needed for a property
    def prop_annotation(self, identifier):
        return "@JsonProperty(\"" + identifier + "\")" if self.annotation_config else None
    
    # Build getter and setter for a property
    def bld_prop_methods(self, prop):
        lines = []
        annote = self.prop_annotation(prop.identifier)
        if annote: lines.append(annote)
        lines.append("public " + prop.kind + " get" + utils.cap_first(prop.identifier) + "() {")
        lines.append("    return this." + prop.identifier + ";")
        lines.append("}")
        if annote: lines.append(annote)
        setter = "public void set" + utils.cap_first(prop.identifier)
        setter += "(final " + prop.kind + ' ' + prop.identifier + ") {"
        lines.append(setter)
        lines.append("    this." + prop.identifier + " = " + prop.identifier + ";")
        lines.append("}")
        return "\n    " + "\n    ".join(lines)

    # Build class declaration -> ex: "public class Cat extends Animal {"
    def bld_class_dec(self, model):
        dec = model.access + " class " + model.identifier
        if len(model.inheritance) > 0:
            dec += " extends "
            parents = ""
            for parent in model.inheritance:
                parents += ", " + parent.split('/')[-1]
            dec += parents[2:]
        return dec + " {"
    
    # Build package reference -> ex: "com.barrettotte.models"
    def bld_namespace(self, obj_path):
        rel_pkg = '.'.join([op.lower() for op in obj_path[:-1]])
        rel_pkg = '.' + rel_pkg if (len(rel_pkg) > 0) else rel_pkg
        return self.project_pkg + rel_pkg

    # Build extends statement
    def bld_inheritance(self, schema):
        extends = []
        if "extends" in schema:
            parent = schema["extends"]
            if "$ref" in parent:
                extends.append(parent["$ref"][:-5])
        return extends

    # Build list of import statements -> ex: "com.barrettotte.models.common.Person"
    def bld_imports(self, items, obj_path):
        imports = []
        for item in items:
            split = item.split('/')
            rel_path = split[:-1]
            if obj_path != rel_path:
                path = [s.lower() for s in rel_path] + [split[-1]]
                imports.append(self.project_pkg + '.' + '.'.join(path).replace('/','.'))
        return imports

    # Build list of properties and list of necessary imports
    def bld_props(self, schema):
        props,imports = ([],[])
        for key,val in schema["properties"].items():
            t = self.get_type(val)
            imp = self.get_obj_import(t)
            p = Property(key, t, "private")
            if "items" in val and "maxItems" in val["items"]:
                p.max_items = val["items"]["maxItems"]
            if "default" in val:
                p.default = val["default"]
            if "parseTo" in val:
                self.get_obj_import(p.kind)
            props.append(p)
            if imp: imports += [i for i in imp if not i in imports]
        return [props,imports]

    # Build class level annotations and list of imports needed for them  
    def bld_annotations(self):
        annotations, imports = ([],[])
        if self.annotation_config and self.annotation_config["type"] == "jackson2":
            imports = self.get_annotation_imports(self.annotation_config["type"])
            if "includes" in self.annotation_config.keys():
                for inc in self.annotation_config["includes"]:
                    annotations.append("@JsonInclude(JsonInclude.Include." + inc + ")")
        return [annotations,imports]

    # Get import statements for annotations
    def get_annotation_imports(self, annotation_type):
        if annotation_type == "jackson2":
            return ["com.fasterxml.jackson.annotation.JsonInclude","com.fasterxml.jackson.annotation.JsonProperty"]
        return []

    # Attempt to parse property to non-standard JSON schema type
    def attempt_parse(self, val):
        p = val["parseTo"].lower()
        if val["type"] == "number" and p == "decimal":                return "BigDecimal"
        if val["type"] == "number" and p in ["double","float"]:       return val["parseTo"]
        if val["type"] == "integer" and p in ["byte","short","long"]: return val["parseTo"]
        if val["type"] == "string" and p in ["char","character"]:     return val["parseTo"]
        warnings.warn("Could not parse '" + val["type"] + "' to '" + val["parseTo"] + "'", 
            SyntaxWarning, stacklevel=10
        )
        return None
    
    # Convert JSON schema type or ref to Java type
    def get_type(self, val):
        if "$ref" in val:
            return val["$ref"]
        if "parseTo" in val:
            attempt = self.attempt_parse(val)
            if attempt: return attempt
        t = val["type"]
        if t == "array":
            return self.get_collection(val)
        if "primitive" in val and val["primitive"]:
            return self.get_primitive(val)
        if t == "string":  return "String"
        if t == "number":  return "Float"
        if t == "integer": return "Integer"
        if t == "boolean": return "Boolean"
        if t == "object":  return "Object"
        raise Exception("Invalid type '" + t + "'")

    # Convert JSON schema collection to java collection
    def get_collection(self, val):
        collection = ''
        if "items" in val:
            items = val["items"]
            t = self.get_type(items)
            if "primitive" in val and val["primitive"]:
                return t + "[]"
            if "uniqueItems" in items and items["uniqueItems"]:
                return "Set<" + t + ">"
            return "List<" + t + ">"
        raise Exception("Could not generate array")
    
    # Convert JSON schema primitive to java primitive
    def get_primitive(self, val):
        t = val["type"]
        if t == "integer": return "int"
        if t == "number":  return "float"
        if t == "boolean": return "boolean"
        if t == "string":  return "String"
        raise Exception("Cannot produce primitive for type '" + t + "'")

    # Return import statement for java object
    def get_obj_import(self, val):
        key = val.lower()
        if "list<" in key: key = "list"
        if "set<"  in key: key = "set"
        if "map<"  in key: key = "map"
        imports = {
            "list":       ["java.util.List", "java.util.ArrayList"],
            "map":        ["java.util.Map" , "java.util.HashMap"],
            "set":        ["java.util.Set" , "java.util.HashSet"],
            "bigdecimal": ["java.math.BigDecimal"]
        }
        return imports[key] if (key in imports) else None