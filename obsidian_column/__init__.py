from mcdreforged.api.all import *
from obsidian_column.config import load_config
from obsidian_column.command.command import load_command

def on_load(server : PluginServerInterface, prev_module):
    # 加载配置文件
    config = load_config(server, prev_module)
    # 加载命令
    load_command(server, config)
    # 注册帮助信息
    server.register_help_message("!!oc", server.rtr("obsidian_column.plugin.mcdr_help_message"), config.permissions.oc)
