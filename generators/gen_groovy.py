import warnings
import utils as utils
from .model import Model,Property
from .gen_java8 import gen_java8

class gen_groovy(gen_java8):

    def __init__(self, config, lang_config):
        gen_java8.__init__(self, config, lang_config)

    def make_code(self, model):
        lines = ["package " + model.namespace + "\n"]
        for imp in model.imports:
            lines.append(("import " + imp) if (len(imp) > 0) else '')
        lines.append('\n' + '\n'.join(model.annotations))
        lines.append(self.bld_class_dec(model) + '\n')
        for prop in model.properties:
            lines.append("    " + self.prop_annotation(prop.identifier))
            p = "    " + prop.kind + " "
            init = self.init_prop(prop)
            p += init if init != '' else prop.identifier
            lines.append(p + "\n")
        lines.append("}")
        return '\n'.join(lines)

    def bld_class_dec(self, model):
        dec = "class " + model.identifier
        if len(model.inheritance) > 0:
            dec += " extends " + model.inheritance[0].split('/')[-1]
        return dec + " {"
