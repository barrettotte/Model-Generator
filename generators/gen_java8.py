
class gen_java8:

    def __init__(self, config, lang_config):
        self.project_pkg = config['jvmPackage']
        self.annotation_config = None
        if "annotation" in lang_config.keys():
            self.annotation_config = lang_config['annotation']

    def bld_pkg_dec(self, obj_path):
        rel_pkg = '.'.join([op.lower() for op in obj_path[:-1]])
        if len(rel_pkg) > 0:
            rel_pkg = '.' + rel_pkg
        return "package " + self.project_pkg + rel_pkg + ';\n'

    def bld_pkg_imp(self, ext_path, obj_path):
        split = ext_path[-1].split('/')
        rel_path = split[:-1]
        imp = ''
        if obj_path != rel_path:
            path = [s.lower() for s in rel_path] + [split[-1]]
            imp = "import " + self.project_pkg + '.' + ".".join(path).replace('/','.') + ';'
        return imp

    def get_extends(self, schema):
        extends = []
        if 'extends' in schema:
            parents = schema['extends']
            extends += [parents[:-5]]
        return extends

    def has_jackson(self):
        return self.annotation_config and self.annotation_config["type"] in ["jackson2"]

    def add_jackson(self):
        jackson = [ "import com.fasterxml.jackson.annotation.JsonInclude;",
          "import com.fasterxml.jackson.annotation.JsonProperty;",
          "import com.fasterxml.jackson.annotation.JsonPropertyOrder;\n"
        ]
        if "includes" in self.annotation_config.keys():
            for inc in self.annotation_config["includes"]:
                jackson.append("@JsonInclude(JsonInclude.Include." + inc + ")")
        return jackson

    def bld_class_head(self, schema, obj_path):
        extends = self.get_extends(schema)
        imports = []

        for ext in extends:
            imp = self.bld_pkg_imp([ext], obj_path[:-1])
            if imp: imports.append(imp)

        header = '\n'.join(imports)
        if len(imports) > 0:
            header += '\n\n'
        if(self.has_jackson()):
            header += '\n'.join(self.add_jackson()) + '\n'
        header += "public class " + obj_path[-1].capitalize()

        if len(extends) > 0:
            header += " extends "
            for ext in extends:
                header += '.'.join(ext[-1]) if len(extends) > 1 else ext.split('/')[-1] 
        return header + " {"

    def bld_props(self, schema):
        props = []
        for key,val in schema['properties'].items():
            props.append("    private " + self.get_java_type(val["type"]) + " " + key + ";\n")
        return '\n' + '\n'.join(props)


    # TODO: Big Decimal, Double
    def get_java_type(self, t):
        if t == 'string':   return "String"
        if t == 'number':   return "float" 
        if t == 'integer':  return "int"
        if t == 'object':   return "Object"
        raise Exception("Invalid java type '" + t + "'")

    def bld_getset(self, schema):
        lines = []
        for key,val in schema['properties'].items():
            prop_type = self.get_java_type(val["type"])
            if self.annotation_config:
                json_prop = "@JsonProperty(\"" + key + "\")"
                
            lines.append("    " + "\n    ".join([
                json_prop,
                "public " + prop_type + " get" + key.capitalize() + "() {",
                "    return " + key + ";",
                "}",
                json_prop,
                "public void set" + key.capitalize() + "(final " + prop_type + ' ' + key + ") {",
                "    this." + key + " = " + key + ';',
                "}"
            ]))
        return "\n\n".join(lines)


    def generate(self, schema, obj_path):
        data = [
            self.bld_pkg_dec(obj_path),
            self.bld_class_head(schema, obj_path),
            self.bld_props(schema) + '\n',
            self.bld_getset(schema),
            '}'
        ]

        model = '\n'.join(data)
        #print(model + '\n')
        return model + '\n'
