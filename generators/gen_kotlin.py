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
            lines.append("    val " + p.identifier + ": " + p.kind)

        lines.append("}\n")
        
        lines.append("class " + model.identifier + " {")
        lines.append("")
        lines.append('}')
        return '\n'.join(lines)

    def bld_class_dec(self, model):
        if len(model.inheritance) > 0:
            return "open class " + model.inheritance[-1].split('/')[-1] + " {"
        return "class " + model.identifier + " {"

    # Set default value for property
    def prop_dft(self, prop):
        dft = ''
        if prop.kind == "String": 
            dft = "\"" + prop.default + "\""
        else:
            dft = str(prop.default)
        return prop.kind + " = " + dft + self.get_suffix(prop.kind)
