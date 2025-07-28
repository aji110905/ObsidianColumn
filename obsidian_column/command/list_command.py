from mcdreforged.command.builder.nodes.basic import Literal

from obsidian_column.command.sub_command import SubCommand

class ListCommand(SubCommand):
    def get_command_node(self) -> Literal:
        return (
            Literal("list")
        )