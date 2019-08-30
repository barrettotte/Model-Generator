import json, os

def get_pretty_json(jsonRaw, sort=False): 
    return json.dumps(jsonRaw, indent=2, sort_keys=sort)

def read_pretty_json(file_path):
    return get_pretty_json(read_file_json(file_path))

def read_file_json(file_path):
    with open(file_path, 'r') as f: return json.load(f)

def write_file_json(file_path, buffer):
    with open(file_path, 'w+') as f: f.write(get_pretty_json(buffer))

def ends_with(s,x):
    return s[-(len(x)):] == x

def mkdir_ine(dir_path):
    if not os.path.exists(dir_path): os.makedirs(dir_path)