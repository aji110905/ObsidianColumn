from typing import List

from mcdreforged.command.command_source import CommandSource
from obsidian_column.config import Config
import time

# 假人组 挖同一个黑曜石柱子的所有假人为一个假人组
class FakePlayerGroup:
    name : str
    all_fake_player_name : List[str] = []
    def __init__(self, x: int, y: int, z: int, radius: int, source : CommandSource, config: Config):
        self.spawn_fake_player(x, y, z, radius, source, config)
        self.name = f"{x}_{z}_{radius}"

    # 召唤假人
    def spawn_fake_player(self, x : int, y : int, z : int, radius : int, source : CommandSource, config : Config):
        # 初始化
        x += 1
        z += radius - 1
        size = radius - 2
        count = 3
        if radius == 6:
            # 第一行
            for i in range(count):
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                time.sleep(config.interval)
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                x -= 1
            x += count + 2
            z -= 1
            count += 4
            # 第二行
            for i in range(count):
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                time.sleep(config.interval)
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                x -= 1
            x += count + 1
            z -= 1
            count += 2
            # 第三四行
            for i in range(2):
                for j in range(count):
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                    self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                    time.sleep(config.interval)
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                    x -= 1
                x += count
                z -= 1
            x += 1
            count += 2
            # 中间三行
            for i in range(3):
                for j in range(count):
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                    self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                    time.sleep(config.interval)
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                    x -= 1
                x += count
                z -= 1
            x -= 1
            count -= 2
            # 倒数三四行
            for i in range(2):
                for j in range(count):
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                    self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                    time.sleep(config.interval)
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                    x -= 1
                x += count
                z -= 1
            x -= 1
            count -= 2
            # 倒数第二行
            for i in range(count):
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                time.sleep(config.interval)
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                x -= 1
            x += count - 2
            z -= 1
            count -= 4
            # 最后一行
            for i in range(count):
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                time.sleep(config.interval)
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                x -= 1
            source.reply(source.get_server().rtr("obsidian_column.command.operation_successful"))
        elif 6 > radius >= 3:
            # 正三角
            for i in range(size + 1):
                for j in range(count):
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                    self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                    time.sleep(config.interval)
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                    x -= 1
                x += count + 1
                count += 2
                z -= 1
            count -= 2
            # 中间一行
            x -= 1
            for i in range(count):
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                time.sleep(config.interval)
                source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                x -= 1
            z -= 1
            x += count - 1
            # 倒三角
            x += 1
            for i in range(size + 1):
                for j in range(count):
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} spawn at {x} {y} {z} facing 0 90 in minecraft:the_end in survival")
                    self.all_fake_player_name.append(f"{config.prefix}{x}_{z}{config.suffix}")
                    time.sleep(config.interval)
                    source.get_server().execute(f"player {config.prefix}{x}_{z}{config.suffix} attack continuous")
                    x -= 1
                x += count - 1
                count -= 2
                z -= 1

            # 提示操作成功
            source.reply(source.get_server().rtr("obsidian_column.plugin_command.spawn.success"))
        else:
            # 半径不对
            source.reply(source.get_server().rtr("obsidian_column.plugin_command.spawn.fail"))
            return