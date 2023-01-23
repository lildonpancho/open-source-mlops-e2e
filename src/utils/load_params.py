import yaml
from box import ConfigBox

def load_params(params_path):
    with open(params_path, "r") as f:
        params = yaml.safe_load(f)
        print(params)
        params = ConfigBox(params)
    return params