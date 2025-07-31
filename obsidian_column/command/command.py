from mcdreforged.api.all import *
from obsidian_column.command.oc_command import OcCommand

def load_command(server: PluginServerInterface):
    server.register_command(OcCommand(server).get_command_node())