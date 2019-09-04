
class gen_base:

    def __init__(self, config, lang_config):
        self.project_pkg = lang_config["namespace"] if "namespace" in lang_config else "./"
        self.annotation_config = None
        if "annotation" in lang_config.keys():
            self.annotation_config = lang_config["annotation"]

    def generate(self, schema, obj_path):
        raise Exception("generate method not implemented!")

    def inject_models(self, model, models_dict):
        raise Exception("inject_models method not implemented!")

    def make_code(self, model):
        raise Exception("make_code method not implemented!")