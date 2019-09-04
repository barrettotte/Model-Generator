import os
import utils as utils

from generators.gen_groovy    import gen_groovy
from generators.gen_java8     import gen_java8
from generators.gen_kotlin    import gen_kotlin
from generators.gen_typescript import gen_typescript


def get_config(path):
    config = utils.read_file_json(path)
    config["schemaDirectory"] = config["schemaDirectory"].replace('/',os.sep).replace('\\',os.sep)
    return config

def validate_config(config):
    pfx = 'Config Validation Error: '
    if not 'schemaDirectory' in config.keys() or (not os.path.exists(config['schemaDirectory'])):
        raise Exception(pfx+'Path to schema directory does not exist.')

def read_schema(fp):
    try:    return utils.read_file_json(fp)
    except: print("Could not read schema at " + fp)

def parse_schema(generator, schema, obj_path):
    model = generator.generate(schema, obj_path)
    return generator.make_code(model)

def get_generator(lang, config):
    return {
        'groovy':     gen_groovy(config, lang),
        'java8':      gen_java8(config, lang),
        'kotlin':     gen_kotlin(config, lang),
        'typescript': gen_typescript(config, lang)
    }[lang['name']]

def split_path(subdir, root):
    split = subdir.split(os.sep)
    rel_path = split[split.index(root):]
    return [] if len(rel_path) == 1 else rel_path[1:]

def make_dir_path(lang, obj_path):
    utils.mkdir_ine(lang["output"])
    dir_path = lang["output"] + os.sep
    if lang["namingConvention"] == "jvm":
        if "namespace" in lang: 
            ns = lang["namespace"].replace('.',os.sep).lower() + os.sep
        else: 
            ns = ''
        utils.mkdir_ine(lang["output"] + os.sep + ns)
        dir_path = dir_path.lower() + ns
    dir_path += os.sep.join(obj_path.split('/')[:-1])
    utils.mkdir_ine(dir_path)
    return dir_path


def main():
    config = get_config("." + os.sep + "config.json")
    validate_config(config)
    in_path = config["schemaDirectory"]
    in_path = in_path[:-1] if utils.ends_with(in_path, os.sep) else in_path
    root = in_path.split(os.sep)[-1]

    for lang in config["languages"]:
        model_dict = {}
        gen = get_generator(lang, config)
        for subdir, _, files in os.walk(in_path):
            for file in files:
                schema = read_schema(os.path.join(subdir, file))
                obj_path = split_path(subdir, root) + [file[:-5]] # ['Common','Thing']
                model = gen.generate(schema, obj_path)
                model_dict[model.ref] = model

        for _,val in model_dict.items():
            model = gen.inject_models(val, model_dict)
            file_path = make_dir_path(lang, model.ref) + os.sep + model.identifier + '.' + lang["extension"]
            with open(file_path, 'w+') as f:
                f.write(gen.make_code(model) + '\n')                    

if __name__ == "__main__" : main()