from mcdreforged.api.all import *
from obsidian_column.config import load_config, get_config
from obsidian_column.command.command import load_command

def on_load(server : PluginServerInterface, prev_module):
    load_config(server, prev_module)
    load_command(server)
    server.register_help_message("!!oc", server.rtr("obsidian_column.plugin_command.plugin_help_message.help_message"), get_config().permissions.oc)

def on_unload(server : PluginServerInterface):
    from obsidian_column.command.oc_command import get_All_FakePlayerGroups
    for FakePlayerGroup in get_All_FakePlayerGroups():
        for name in FakePlayerGroup.all_fake_player_name:
            server.execute(f"player {name} kill")