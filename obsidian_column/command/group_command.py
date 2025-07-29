from mcdreforged.api.all import *
from obsidian_column.command.sub_command import SubCommand
from obsidian_column.config import get_config

class GroupCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal({"group", "g"}).runs(self.show_help_message)
        )

    def show_help_message(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.group):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message.group"):
            source.reply(line)