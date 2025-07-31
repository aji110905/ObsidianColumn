from mcdreforged.api.all import *
from obsidian_column.command.sub_command import SubCommand
from obsidian_column.config import get_config

class GroupCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal({"group", "g"}).runs(self.show_help_message).
            then(Literal({"list", "l"}).runs(self.show_list)).
            then(Literal({"kill", "k"}).then(Text("string").runs(self.kill_group))).
            then(Literal({"attack", "a"}).then(Text("string").runs(self.re_attack)))
        )

    def show_help_message(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.group):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message.group"):
            source.reply(line)

    def show_list(self,source : CommandSource, context: CommandContext):
        from obsidian_column.command.oc_command import All_FakePlayerGroups

        if not self.determine_permissions(source, get_config().permissions.group):
            return
        if not All_FakePlayerGroups:
            source.reply(source.get_server().rtr("obsidian_column.plugin_command.group.list.none"))
            return
        for FakePlayerGroup in All_FakePlayerGroups:
            kill_text = RText("§7[↓]")
            kill_text.set_click_event(RAction.run_command, f"!!oc group kill {FakePlayerGroup.name}")
            kill_text.set_hover_text(source.get_server().rtr("obsidian_column.plugin_command.group.list.show.kill"))

            attack_text = RText("§7[↻]")
            attack_text.set_click_event(RAction.run_command, f"!!oc group attack {FakePlayerGroup.name}")
            attack_text.set_hover_text(source.get_server().rtr("obsidian_column.plugin_command.group.list.show.attack"))

            source.reply(FakePlayerGroup.name + kill_text + " " + attack_text)

    def kill_group(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.group):
            return
        from obsidian_column.command.oc_command import All_FakePlayerGroups
        for FakePlayerGroup in All_FakePlayerGroups:
            if FakePlayerGroup.name == context["string"]:
                for name in FakePlayerGroup.all_fake_player_name:
                    source.get_server().execute(f"player {name} kill")
                All_FakePlayerGroups.remove(FakePlayerGroup)
                source.reply(source.get_server().rtr("obsidian_column.plugin_command.group.kill.success", context["string"]))
                return
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.group.kill.fail"))

    def re_attack(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, get_config().permissions.group):
            return
        from obsidian_column.command.oc_command import All_FakePlayerGroups
        for FakePlayerGroup in All_FakePlayerGroups:
            if FakePlayerGroup.name == context["string"]:
                for name in FakePlayerGroup.all_fake_player_name:
                    source.get_server().execute(f"player {name} attack continuous")
                source.reply(source.get_server().rtr("obsidian_column.plugin_command.group.attack.success", context["string"]))
                return
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.group.attack.fail"))