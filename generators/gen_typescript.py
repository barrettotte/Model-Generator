import warnings
import utils as utils
from .model import Model,Property
from .gen_base import gen_base

class gen_typescript(gen_base):

    def __init__(self, config, lang_config):
        gen_base.__init__(self, config, lang_config)

    # Parse schema and build model
    def generate(self, schema, obj_path):
        model = Model(obj_path[-1], '/'.join(obj_path)+'.json')
        model.inheritance = self.bld_inheritance(schema)
        model.imports = self.bld_imports(model.inheritance, obj_path)
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

    # Generate source code from model
    def make_code(self, model):
        lines = []
        for imp in model.imports:
            if len(imp) > 0:
                intr = imp.split('/')[-1]
                lines.append(("import { " + intr + " } from '" + imp + "'"))
        lines.append('\n' + self.bld_class_dec(model))
        for p in model.properties:
            if p.default:
                prop = ": " + p.kind + " = " + ("'" + str(p.default) + "'" if p.kind == "string" else str(p.default))
            else:
                prop = "?: " + p.kind
            lines.append("    " + p.identifier + prop + ";")
        lines.append("}")
        return '\n'.join(lines)
    
    # Get model reference within collection -> ex:  "List<Common/Thing.json>" = "Common/Thing.json"
    def get_json_ref(self, s):
        return s[s.rfind('<')+1:s.find('>')] if ('<' in s) else s

    # Build extends statement
    def bld_inheritance(self, schema):
        extends = []
        if "extends" in schema:
            parent = schema["extends"]
            if "$ref" in parent:
                extends.append(parent["$ref"][:-5])
        return extends

    # Build list of import statements -> ex: "from './common/Thing'"
    def bld_imports(self, items, obj_path):
        imports = []
        for item in items:
            split = item.split('/')
            rel_path = split[:-1]
            if obj_path != rel_path:
                tmp = ''
                if not type(obj_path) is str:
                    tmp += '../' * (len(obj_path)-1)
                path = [s for s in rel_path] + [split[-1]]
                imports.append((tmp if len(tmp) > 0 else self.project_pkg) + '/'.join(path))
        return imports

    # Build class declaration -> ex: "export interface Cat extends Thing {"
    def bld_class_dec(self, model):
        dec = "export class " + model.identifier
        if len(model.inheritance) > 0:
            dec += " extends "
            parents = ""
            for parent in model.inheritance:
                parents += ", " + parent.split('/')[-1]
            dec += parents[2:]
        return dec + " {"

    # Build list of properties and list of necessary imports
    def bld_props(self, schema):
        props,imports = ([],[])
        for key,val in schema["properties"].items():
            t = self.get_type(val)
            p = Property(key, t, "private")
            if "items" in val and "maxItems" in val["items"]:
                p.max_items = val["items"]["maxItems"]
            if "default" in val:
                p.default = val["default"]
            props.append(p)
        return [props,imports]

    # Convert JSON schema type or ref to typescript type
    def get_type(self, val):
        if "$ref" in val:
            return val["$ref"]
        t = val["type"]
        if t == "array":
            return self.get_collection(val)
        if t in ["string","boolean","number","object"]:  return t
        if t == "integer": return "number"
        raise Exception("Invalid type '" + t + "'")

    # Convert JSON schema collection to typescript collection
    def get_collection(self, val):
        collection = ''
        if "items" in val:
            items = val["items"]
            t = self.get_type(items)
            if "primitive" in val and val["primitive"]:
                return t + "[]"
            return "Array<" + t + ">"
        raise Exception("Could not generate array")