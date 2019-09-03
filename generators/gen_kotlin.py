import warnings
import utils as utils
from .model import Model,Property
from .gen_java8 import gen_java8

class gen_kotlin(gen_java8):

    def __init__(self, config, lang_config):
        gen_java8.__init__(self, config, lang_config)

    def make_code(self, model):
        lines = ["package " + model.namespace + '\n']
        #for imp in model.imports:
        #    lines.append(("import " + imp + ";") if (len(imp) > 0) else '')
        #lines.append('\n' + '\n'.join(model.annotations))
        lines.append(self.bld_class_dec(model))

        for p in model.properties:
            init =  self.init_prop(p)
            lines.append("    var " + p.identifier + ": " + p.kind + (init if init else ''))

        lines.append("}\n")
        
        lines.append("class " + model.identifier + " {")
        lines.append("")
        lines.append('}')
        return '\n'.join(lines)

    def bld_class_dec(self, model):
        if len(model.inheritance) > 0:
            return "open class " + model.inheritance[-1].split('/')[-1] + " {"
        return "class " + model.identifier + " {"

    def init_prop(self, prop):
        if prop.default:
            dft = str(prop.default) if prop.kind != "String" else str("\""+prop.default+"\"")
            return " = " + dft
        if "[]" in prop.kind:
            if prop.max_items:
                kind = prop.kind.replace("[]", "[" + str(prop.max_items) + "]")
                return " = " + kind
            raise Exception("Cannot initialize primitive array '" + str(prop) + "' without 'maxItems' declared.")
        exclude = ["String","Integer","int","Double","double","Boolean","boolean","Float","float"]
        if not prop.kind in exclude:
            kind = prop.kind
            if "List<" in kind: kind = kind.replace("List<","ArrayList<")
            if "Map<"  in kind: kind = kind.replace("Map<","HashMap<")
            if "Set<"  in kind: kind = kind.replace("Set<","HashSet<")
            return prop.identifier + " = " + kind + "()"
        return None
