from mcdreforged.api.all import *
from obsidian_column.command.oc_command import OcCommand
from obsidian_column.config import Config

def load_command(server: PluginServerInterface, config: Config):
    # 注册命令
    server.register_command(OcCommand(server, config).get_command_node())