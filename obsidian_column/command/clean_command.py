from obsidian_column.command.sub_command import SubCommand
from mcdreforged.api.all import *
from obsidian_column.config import get_config

class CleanCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal({"clean", "c"}).runs(self.show_help_message).
            then(Literal({"prefix", "pre"}).runs(self.clean_prefix)).
            then(Literal({"suffix", "suf"}).runs(self.clean_suffix))
        )

    def show_help_message(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.clean):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message.clean"):
            source.reply(line)

    def clean_prefix(self,source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.clean):
            return
        self.save_config(get_config(), "prefix", self.server, "")
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.clean.prefix.success"))

    def clean_suffix(self,source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.clean):
            return
        self.save_config(get_config(), "suffix", self.server, "")
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.clean.suffix.success"))