# ======= File: resources.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/6 14:15
# @Desc : 项目目录以及资源


"""
资源后加了 `###` 三个井号的为需要修改成本地的信息
"""

"""软件"""
SOFTWARE_ARR = ['IDEA', 'VMware', 'XShell', 'VScode']
"""json文件"""
JSON_FILE_PATH = r'config.json'

"""
IDEA
"""
# idea启动项，因为将IDEA的bin目录配置在了环境变量中，如果没有，需要指定真实路径
IDEA_EXT = "idea64.exe" ###
# idea的日志文件路径
LOG_FILE_PATH_IDEA = r'C:\Users\dell\AppData\Local\JetBrains\IntelliJIdea2023.2\log\idea.log' ###
# 关键字，不需要修改
KEYWORD_IDEA = "Finished for"


"""
VMware
"""
# todo 窗口上没有输入ip的输入框，目前只能选择一个虚拟机
# 虚拟机的 IP 地址
VM_IP = "192.168.139.3" ###
# vm 启动项
VM_EXE = r"C:\download_app\vmware.exe" ###


"""
Xshell
"""
# xshell启动项
Xshell_EXE = r"D:\download_app_2024\spark\xshell\Xshell.exe"    ###
# 关键字，不需要修改
KEYWORD_XSHELL = "Session Name"
# xshell的日志文件路径
# 注意session的名字尽量避免中文，否则程序会因无法解析而报错，不好处理
LOG_FILE_PATH_XSHELL = r'D:\DIC2024\XShell-log\Connection.log'  ###
# 图片路径，用于识别选择哪一个虚拟机
# 要连接的虚拟机名称要与输入框输入的名称一致，这里的图片名称为了区分，尽量都一致就对了
TEMPLATE_PATH_VM = "../photoes/vm.jpg"  ###


"""
VScode
"""
# vs启动项
VSCODE_EXE = r"D:\download_app_2024\VS Code\Code.exe"


"""
其他待定
"""