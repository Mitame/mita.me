import json
from binascii import b2a_hex
from os import urandom

from . import app

DEFAULT_CONFIG_PATH = "./config.json"

default_config = {
    "allow_config_writing": True,
    
    "port": 5000,
    "bind_addr": "0.0.0.0",
    "secret_key": b2a_hex(urandom(32)).decode("utf8"),
    "debug": False,

    "mongo": {
        "host": "localhost",
        "port": 27017,
        "db": "mita_site",
    }
}


def merge_dicts(a, b):
    """Use a as base, overwrite with items from b"""
    new_dict = a
    for key, value in b.items():
        if isinstance(value, dict):
            if key in a:
                merge_dicts(a[key], b[key])
            else:
                a[key] = b[key]
        else:
            a[key] = b[key]

    return new_dict


def save_config(file_path=DEFAULT_CONFIG_PATH, config_dict=None, force=False):
    global config
    if config_dict is None:
        config_dict = config
    else:
        config = config_dict

    if config["allow_config_writing"] or force:
        json.dump(
            config_dict,
            open(file_path, "w"),
            sort_keys = True,
            indent = 2,
            separators = (',', ': ')
        )


try:
    loaded_config = json.load(open(DEFAULT_CONFIG_PATH))
    config = merge_dicts(default_config, loaded_config)
except IOError:
    print("Config file not found. Loading defaults...")
    print("You should probably edit the config file with your settings.")
    config = default_config

save_config()

app.secret_key = config["secret_key"]
