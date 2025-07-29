from typing import List
from mcdreforged.api.all import *
from obsidian_column.FakePlayerGroup import FakePlayerGroup
from obsidian_column.command.clean_command import CleanCommand
from obsidian_column.command.group_command import GroupCommand
from obsidian_column.command.set_command import SetCommand
from obsidian_column.command.sub_command import SubCommand

class OcCommand(SubCommand):
    all_FakePlayerGroups: List[FakePlayerGroup] = []
    def get_command_node(self) -> Literal:
        main_main_sub_command = (
            Literal("!!oc").runs(self.show_help_message).
            then(Literal({"reload", "r"}).runs(self.reload_plugin)).
            then(Literal({"config", "con"}).runs(self.show_now_config)).
            then(Literal("spawn").then(Integer("x").then(Integer("y").then(Integer("z").then(Integer("radius").runs(self.spawn_fake_player_attack))))))
        )
        main_main_sub_command.then(SetCommand(self.server, self.config).get_command_node())
        main_main_sub_command.then(CleanCommand(self.server, self.config).get_command_node())
        main_main_sub_command.then(GroupCommand(self.server, self.config).get_command_node())
        return main_main_sub_command

    # 显示帮助信息
    def show_help_message(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.set):
            return
        for line in self.get_help_message(source, "obsidian_column.plugin_command.plugin_help_message"):
            source.reply(line)

    #重载插件
    def reload_plugin(self, source : CommandSource, context: CommandContext):
        if not self.determine_permissions(source, self.config.permissions.reload):
            return
        source.get_server().reload_plugin("obsidian_column")
        source.reply(source.get_server().rtr("obsidian_column.plugin_command.reload.success"))

    def show_now_config(self, source : CommandSource, context: CommandContext):
        source.reply(source.get_server().rtr(
            "obsidian_column.plugin_command.config",
            self.config.interval,
            self.config.prefix,
            self.config.suffix)
        )

    # 批量召唤假人挖掘黑曜石柱
    @new_thread("spawn") # 创建新的线程 避免看门狗报错
    def spawn_fake_player_attack(self, source : CommandSource, context: CommandContext):
        # 判断权限是否足够
        if not self.determine_permissions(source, self.config.permissions.spawn):
            return
        self.all_FakePlayerGroups.append(FakePlayerGroup(context["x"], context["y"], context["z"], context["radius"], source, self.config))
