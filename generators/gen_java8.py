import utils as utils
from .model import Model,Property

class gen_java8:

    def __init__(self, config, lang_config):
        self.project_pkg = config['jvmPackage']
        self.annotation_config = None
        if "annotation" in lang_config.keys():
            self.annotation_config = lang_config["annotation"]

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
    
    def get_json_ref(self, s):
        return s[s.rfind('<')+1:s.find('>')] if ('<' in s) else s

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

    def bld_dft_ctor(self, model):
        lines = []
        lines.append("public " + model.identifier + "() {")
        for p in model.properties:
            init = self.init_prop(p)
            if init: lines.append(init)
        lines.append("}")
        return "\n    " + "\n    ".join(lines)

    def init_prop(self, prop):
        exclude = ["String","Integer","int","Double","double","Boolean","boolean","Float","float"]
        if "[]" in prop.kind:
            if prop.max_items:
                kind = prop.kind.replace("[]", "[" + str(prop.max_items) + "]")
                return "    this." + prop.identifier + " = new " + kind + ";"

            raise Exception("Cannot initialize primitive array '" + str(prop) + "' without 'maxItems' declared.")
        if not prop.kind in exclude:
            kind = prop.kind
            if "List<" in kind: kind = kind.replace("List<","ArrayList<")
            if "Map<"  in kind: kind = kind.replace("Map<","HashMap<")
            if "Set<"  in kind: kind = kind.replace("Set<","HashSet<")
            return "    this." + prop.identifier + " = new " + kind + "();"
        return None
    
    def bld_prop_methods(self, prop):
        lines = []
        ant = "@JsonProperty(\"" + prop.identifier + "\")" if self.annotation_config else None
        if ant: lines.append(ant)
        lines.append("public " + prop.kind + " get" + utils.cap_first(prop.identifier) + "() {")
        lines.append("    return this." + prop.identifier + ";")
        lines.append("}")
        if ant: lines.append(ant)
        setter = "public void set" + utils.cap_first(prop.identifier)
        setter += "(final " + prop.kind + ' ' + prop.identifier + ") {"
        lines.append(setter)
        lines.append("    this." + prop.identifier + " = " + prop.identifier + ";")
        lines.append("}")
        return "\n    " + "\n    ".join(lines)

    def bld_class_dec(self, model):
        dec = model.access + " class " + model.identifier
        if len(model.inheritance) > 0:
            dec += " extends "
            parents = ""
            for parent in model.inheritance:
                parents += ", " + parent.split('/')[-1]
            dec += parents[2:]
        return dec + " {"
    
    def bld_namespace(self, obj_path):
        rel_pkg = '.'.join([op.lower() for op in obj_path[:-1]])
        rel_pkg = '.' + rel_pkg if (len(rel_pkg) > 0) else rel_pkg
        return self.project_pkg + rel_pkg

    def bld_inheritance(self, schema):
        extends = [] # TODO add multiple inheritance
        if "extends" in schema:
            parent = schema["extends"]
            if "$ref" in parent:
                extends.append(parent["$ref"][:-5]) # removes '.json'
        return extends

    def bld_imports(self, items, obj_path):
        imports = []
        for item in items:
            split = item.split('/')
            rel_path = split[:-1]
            if obj_path != rel_path:
                path = [s.lower() for s in rel_path] + [split[-1]]
                imports.append(self.project_pkg + '.' + '.'.join(path).replace('/','.'))
        return imports

    def bld_props(self, schema):
        props,imports = ([],[])
        for key,val in schema["properties"].items():
            t = self.java_type(val)
            imp = self.java_import(t)
            p = Property(key, t, "private")
            if "items" in val and "maxItems" in val["items"]:
                p.max_items = val["items"]["maxItems"]
            props.append(p)    
            if imp: imports += [i for i in imp if not i in imports]
        return [props,imports]
        
    def bld_annotations(self):
        annotations, imports = ([],[])
        if self.annotation_config and self.annotation_config["type"] == "jackson2":
            imports = [
              "com.fasterxml.jackson.annotation.JsonInclude",
              "com.fasterxml.jackson.annotation.JsonProperty",
              "com.fasterxml.jackson.annotation.JsonPropertyOrder"
            ]
            if "includes" in self.annotation_config.keys():
                for inc in self.annotation_config["includes"]:
                    annotations.append("@JsonInclude(JsonInclude.Include." + inc + ")")
        return [annotations,imports]

    def java_type(self, val):
        if "$ref" in val:
            return val["$ref"]
        t = val["type"]
        if t == "array":
            return self.java_collection(val)
        if "primitive" in val and val["primitive"]:
            return self.java_primitive(val)
        if t == "string":  return "String"
        if t == "number":  return "Float"
        if t == "integer": return "Integer"
        if t == "boolean": return "Boolean"
        if t == "object":  return "Object"
        raise Exception("Invalid type '" + t + "'")

    def java_collection(self, val):
        collection = ''
        if "items" in val:
            items = val["items"]
            t = self.java_type(items)
            if "primitive" in items and items["primitive"]:
                return t + "[]"
            if "uniqueItems" in items and items["uniqueItems"]:
                return "Set<" + t + ">"
            return "List<" + t + ">"
        raise Exception("Could not generate array")
    
    def java_primitive(self, val):
        t = val["type"]
        if t == "integer": return "int"
        if t == "number":  return "float"
        if t == "boolean": return "boolean"
        raise Exception("Cannot produce primitive for type '" + t + "'")

    def java_import(self, val):
        key = val.lower()
        if "list<" in key: key = "list"
        if "set<"  in key: key = "set"
        if "map<"  in key: key = "map"
        imports = {
            "list": ["java.util.List", "java.util.ArrayList"],
            "map":  ["java.util.Map" , "java.util.HashMap"],
            "set":  ["java.util.Set" , "java.util.HashSet"]
        }
        return imports[key] if (key in imports) else None