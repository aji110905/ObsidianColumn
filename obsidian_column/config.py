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

def load_config(server : PluginServerInterface, prev_module) -> Config:
    if prev_module is None:
        config = Config()
        server.save_config_simple(config)
        return config
    else:
        return server.load_config_simple(target_class = Config())