from obsidian_column.command.sub_command import SubCommand
from mcdreforged.api.all import *

class SetCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal({"set", "s"}).runs(self.show_help_message).
            then(Literal({"interval", "i"}).then(Integer("number").runs(self.set_interval))).
            then(Literal({"prefix", "pre"}).then(Integer("number").runs(self.set_prefix))).
            then(Literal({"suffix", "suf"}).then(Integer("number").runs(self.set_suffix)))
        )

    def show_help_message(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.set):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message.set"):
            source.reply(line)

    def set_interval(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.set):
            return
        if context["number"] < 0:
            source.reply(source.get_server().rtr("obsidian_column.plugin_command.interval.negative_number_error"))
            return
        self.config = self.save_config(self.config, "interval", self.server, context["number"])
        source.reply(source.get_server().rtr("obsidian_column.command.set.interval.success", self.config.interval))

    def set_prefix(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.set):
            return
        self.config = self.save_config(self.config, "prefix", self.server, context["string"])
        source.reply(source.get_server().rtr("obsidian_column.command.set.prefix.success", self.config.prefix))

    def set_suffix(self, source: CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.set):
            return
        self.config = self.save_config(self.config, "suffix", self.server, context["string"])
        source.reply(source.get_server().rtr("obsidian_column.command.set.suffix.success", self.config.suffix))