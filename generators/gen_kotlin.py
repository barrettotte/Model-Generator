import warnings
import utils as utils
from .model import Model,Property
from .gen_java8 import gen_java8

class gen_kotlin(gen_java8):

    def __init__(self, config, lang_config):
        gen_java8.__init__(self, config, lang_config)

    def make_code(self, model):
        lines = ["package " + model.namespace + '\n']
        for imp in model.imports:
            lines.append(("import " + imp) if (len(imp) > 0) else '')

        lines.append('\n' + '\n'.join(model.annotations))
        lines.append(self.bld_class_dec(model))
        for p in model.properties:
            init =  self.init_prop(p)
            lines.append("    var " + p.identifier + ": " + p.kind + init)
        lines.append("}")
        return '\n'.join(lines)

    def bld_class_dec(self, model):
        dec = "open class " + model.identifier
        if len(model.inheritance) > 0:
            dec += " : " + model.inheritance[0].split('/')[-1]
        return dec + " {"

    # Set default value for property
    def prop_dft(self, prop):
        dft = ''
        if prop.kind == "String": 
            dft = "\"" + prop.default + "\""
        else:
            dft = str(prop.default)
        return " = " + dft + self.get_suffix(prop.kind)

    # Default params for new obj -> ex: val bd: = BigDecimal(0)
    def init_obj(self, prop):
        kind = self.collection_impl(prop.kind)
        obj_suffix = "()"
        if kind == "BigDecimal": obj_suffix = "(0)"
        return " = " + kind + obj_suffix

    # Kotlin doesn't have long,int,float,etc
    def get_primitive(self, val):
        return val["type"]

    # Convert JSON schema collection to kotlin collection
    def get_collection(self, val):
        collection = ''
        if "items" in val:
            items = val["items"]
            t = self.get_type(items)
            if "primitive" in val and val["primitive"]:
                return "Array<" + t + ">"
            if "uniqueItems" in items and items["uniqueItems"]:
                return "Set<" + t + ">"
            return "List<" + t + ">"
        raise Exception("Could not generate array")
    
    # Get import statements for annotations
    def get_annotation_imports(self, annotation_type):
        if annotation_type == "jackson2":
            return ["com.fasterxml.jackson.module.kotlin.*"]
        return []

    # Convert JSON schema type or ref to Kotlin type
    def get_type(self, val):
        if "$ref" in val:
            return val["$ref"]
        if "parseTo" in val:
            attempt = self.attempt_parse(val)
            if attempt: return attempt
        t = val["type"]
        if t == "array":   return self.get_collection(val)
        if t == "string":  return "String"
        if t == "number":  return "Float"
        if t == "integer": return "Int"
        if t == "boolean": return "Boolean"
        if t == "object":  return "Object"
        raise Exception("Invalid type '" + t + "'")

    # Return import statement for java object
    def get_obj_import(self, val):
        key = val.lower()
        imports = {} # none needed so far, kotlin imports a lot by default
        return imports[key] if (key in imports) else None

    # Attempt to parse property to non-standard JSON schema type
    def attempt_parse(self, val):
        p = val["parseTo"].capitalize()
        if val["type"] == "number"  and p ==  "Decimal":               return "BigDecimal"
        if val["type"] == "number"  and p in ["Double","Float"]:       return p
        if val["type"] == "integer" and p in ["Byte","Short","Long"]:  return p
        if val["type"] == "string"  and p ==  "Char":                  return p
        warnings.warn("Could not parse '" + val["type"] + "' to '" + val["parseTo"] + "'", 
            SyntaxWarning, stacklevel=10
        )
        return None

    # Check if type is not a primitive value
    def is_complex_type(self, kind):
        return not kind in ["String","Int","Double","Boolean","Float","Byte","Short","Long","Char"]

     # Implement collection interfaces
    def collection_impl(self, kind):
        impl = kind
        if "List<" in kind:  impl = impl.replace("List<","MutableList<")
        if "Map<"  in kind:  impl = impl.replace("Map<","MutableMap<")
        if "Set<"  in kind:  impl = impl.replace("Set<","MutableSet<")
        return impl