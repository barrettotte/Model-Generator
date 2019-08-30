import os
import utils as utils

from generators.gen_java8 import gen_java8

def get_config(path):
    return utils.read_file_json(path)

def validate_config(config):
    pfx = 'Config Validation Error: '
    if not 'schemaDirectory' in config.keys() or (not os.path.exists(config['schemaDirectory'])):
        raise Exception(pfx+'Path to schema directory does not exist.')

def read_schema(fp):
    try:    return utils.read_file_json(fp)
    except: print("Could not read schema at " + fp)

def parse_schema(lang, schema, obj_path, config):
    generator = {
        'java8': gen_java8(config)
    }[lang['name']]
    return generator.generate(schema, obj_path)

def slice_path(subdir, root):
    split = subdir.split("\\")
    rel_path = split[split.index(root):]
    return [] if len(rel_path) == 1 else rel_path[1:]


def main():
    config = get_config("./config.json")
    validate_config(config)
    in_path = config['schemaDirectory']
    in_path = in_path[:-1] if utils.ends_with(in_path, "\\") else in_path

    root = in_path.split('\\')[-1]

    out = ''
    for subdir, _, files in os.walk(in_path):
        for file in files:
            schema = read_schema(os.path.join(subdir, file))
            for lang in config['languages']:
                obj_path = slice_path(subdir, root) + [file[:-5]] # ['Common','Thing']
                
                out += (parse_schema(lang, schema, obj_path, config) + "\n")

    with open('test.txt', 'w+') as f:
        f.write(out)

if __name__ == "__main__" : main()