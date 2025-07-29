from mcdreforged.api.all import *

class PermissionConfig(Serializable):
    oc : int = 1
    spawn : int = 1
    reload : int = 1
    group: int = 1
    set : int = 2
    clean : int = 2

class Config(Serializable):
    interval : int = 5
    prefix : str = ""
    suffix : str = ""
    permissions : PermissionConfig = PermissionConfig()

config : Config
server : PluginServerInterface

def load_config(server_ : PluginServerInterface, prev_module) -> Config:
    global config, server
    if prev_module is None:
        server = server_
        config = Config()
        server.save_config_simple(config)
        return config
    else:
        server = server_
        config = server.load_config_simple(target_class = Config())
        return config

def get_config() -> Config:
    global config
    return config

def reload_config():
    global config, server
    config = server.load_config_simple(target_class=Config())