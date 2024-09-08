# ======= File: resources.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/6 14:15
# @Desc : 项目目录以及资源


"""
IDEA
"""
# idea启动项，因为将IDEA的bin目录配置在了环境变量中，如果没有，需要指定真实路径
IDEA_EXT = "idea64.exe"
# idea项目路径
IDEA_HMDP_PATH = r"D:\ITHEIMA\hm-dianping"
# 关键字，不需要修改
KEYWORD_IDEA = "Finished for"
# idea的日志文件路径
LOG_FILE_PATH_IDEA = r'C:\Users\dell\AppData\Local\JetBrains\IntelliJIdea2023.2\log\idea.log'


"""
VMware
"""
# 虚拟机的 IP 地址
VM_IP = "192.168.139.3"
# vm 启动项
VM_EXE = r"C:\download_app\vmware.exe"
# vm 虚拟机的路径，我的虚拟机名为
VM_DOCKER_PATH = r"C:\dowmload_app_vm\centos_dic\new2024_06_05for_learn\CentOS 7 64 位.vmx"


"""
Xshell
"""
# xshell启动项
Xshell_EXE = r"D:\download_app_2024\spark\xshell\Xshell.exe"
# 关键字，不需要修改
KEYWORD_XSHELL = "Session Name"
# KEYWORD_XSHELL = "Connected to 192.168.139.3:22/SSH"
# xshell的日志文件路径
# 注意session的名字尽量避免中文，否则程序会因无法解析而报错，不好处理
LOG_FILE_PATH_XSHELL = r'D:\DIC2024\XShell-log\Connection.log'
# 图片路径，用于识别选择哪一个虚拟机
TEMPLATE_PATH_VM = "../photoes/vm.jpg"

"""
其他待定
"""