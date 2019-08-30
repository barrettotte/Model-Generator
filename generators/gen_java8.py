
class gen_java8:

    def __init__(self, config):
        self.project_pkg = config['jvmPackage']

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

    def bld_class_head(self, schema, obj_path):
        header = ''
        imports = []
        extends = self.get_extends(schema)
        for ext in extends:
            imp = self.bld_pkg_imp([ext], obj_path[:-1])
            if imp: imports.append(imp)
        header += '\n'.join(imports)
        if len(imports) > 0:
            header += '\n\n'
        header += "public class " + obj_path[-1].capitalize()

        if len(extends) > 0:
            header += " extends "
            for ext in extends:
                header += '.'.join(ext[-1]) if len(extends) > 1 else ext.split('/')[-1] 
        return header + " {"

    
    def generate(self, schema, obj_path):
        data = [
            self.bld_pkg_dec(obj_path),
            self.bld_class_head(schema, obj_path),
            '\n}'
        ]
        model = '\n'.join(data)
        print(model + '\n')
        
        return model+'\n\n\n'


