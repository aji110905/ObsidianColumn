# ObsidianColumn

## 简介

Obsidian Column 是一款基于 [MCDReforged](https://github.com/MCDReforged/MCDReforged) 的插件，能够帮助你在 Minecraft 中召唤大量假人自动挖掘末地黑曜石柱

## 依赖

依赖模组[Carpet](https://modrinth.com/mod/carpet)

## 功能特点

- 召唤多个假人组进行黑曜石柱挖掘
- 可配置假人召唤间隔、前缀和后缀
- 支持假人组管理（列出、清除、重新挖掘）

## 命令说明

### 基础命令

- `!!oc`: 显示帮助信息
- `!!oc reload`: 重载插件
- `!!oc config`: 显示当前配置信息
- `!!oc spawn <x> <y> <z> <半径>`: 召唤假人组挖掘黑曜石柱

### 设置命令

- `!!oc set`: 显示设置相关帮助信息
- `!!oc set interval <整数>`: 设置每召唤一个假人的间隔时间
- `!!oc set prefix <字符串>`: 设置假人名称前缀
- `!!oc set suffix <字符串>`: 设置假人名称后缀

### 清除命令

- `!!oc clean`: 显示清除相关帮助信息
- `!!oc clean prefix`: 清除假人前缀
- `!!oc clean suffix`: 清除假人后缀

### 假人组命令

- `!!oc group`: 显示假人组相关帮助信息
- `!!oc group list`: 显示所有假人组
- `!!oc group kill <组名>`: 清除指定假人组
- `!!oc group attack <组名>`: 让指定假人组重新开始挖掘

## 配置说明

插件配置包含以下可调整项：

- `interval`: 假人召唤间隔时间（默认值：5）
- `prefix`: 假人名称前缀（默认值：空）
- `suffix`: 假人名称后缀（默认值：空）

权限等级说明：
- `oc`: 使用基础命令的权限等级（默认值：1）
- `spawn`: 使用召唤假人命令的权限等级（默认值：1）
- `reload`: 使用重载插件命令的权限等级（默认值：1）
- `group`: 使用假人组管理命令的权限等级（默认值：1）
- `set`: 使用设置命令的权限等级（默认值：2）
- `clean`: 使用清除命令的权限等级（默认值：2）

## 注意事项

- 卸载插件时会自动清除所有已召唤的假人