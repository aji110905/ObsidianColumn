from obsidian_column.command.sub_command import SubCommand
from mcdreforged.api.all import *
from obsidian_column.config import get_config

class SetCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal({"set", "s"}).runs(self.show_help_message).
            then(Literal({"interval", "i"}).then(Integer("number").runs(self.set_interval))).
            then(Literal({"prefix", "pre"}).then(Text("string").runs(self.set_prefix))).
            then(Literal({"suffix", "suf"}).then(Text("string").runs(self.set_suffix)))
        )

    def show_help_message(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.set):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message.set"):
            source.reply(line)

    def set_interval(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.set):
            return
        if context["number"] < 0:
            source.reply(source.get_server().rtr("obsidian_column.plugin_command.set.interval.negative_number_error"))
            return
        self.save_config(get_config(), "interval", self.server, context["number"])
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.set.interval.success", get_config().interval))

    def set_prefix(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.set):
            return
        self.save_config(get_config(), "prefix", self.server, context["string"])
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.set.prefix.success", get_config().prefix))

    def set_suffix(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.set):
            return
        self.save_config(get_config(), "suffix", self.server, context["string"])
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.set.suffix.success", get_config().suffix))