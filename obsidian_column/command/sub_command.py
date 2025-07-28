import re
from abc import ABC, abstractmethod
from typing import List
from mcdreforged.api.all import *
from obsidian_column.config import Config

class SubCommand(ABC):
    def __init__(self,server : PluginServerInterface, config : Config):
        self.server = server
        self.config = config

    @abstractmethod
    def get_command_node(self) -> Literal:
        raise NotImplementedError()

    def determine_permissions(self, source: CommandSource, operate: int) -> bool:
        if source.is_player and not source.has_permission(operate):
            source.reply(source.get_server().rtr("mcdreforged.mcdr_command.permission_denied"))
            return False
        else:
            return True

    def save_config(self, config: Config, type: str, server: PluginServerInterface, new_value, ) -> Config:
        setattr(config, type, new_value)
        server.save_config_simple(config)
        return config

    def get_help_message(self, source: CommandSource, translation_key: str) -> List[RTextBase]:
        list = []
        for line in source.get_server().rtr(translation_key).to_plain_text().splitlines(keepends=False):
            prefix = re.search(r'(?<=§7)' + "!!oc" + r'[\w ]*(?=§)', line)
            if prefix is not None:
                list.append(RText(line).c(RAction.suggest_command, prefix.group()))
            else:
                list.append(line)
        return list # 返回装有着帮助信息富文本的list集合