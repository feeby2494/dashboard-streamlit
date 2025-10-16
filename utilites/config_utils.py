import yaml
from yaml.loader import SafeLoader

#save new config; overwrite with original yaml and new stuff added to it
def save_config(file, new_config):
    with open(file, "w") as file:
        yaml.dump(new_config, file)

# load the secure yaml
def load_config(file):
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
    return config