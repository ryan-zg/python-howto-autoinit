# ======= File: method.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/6 14:27
# @Desc : 方法api

import os
import psutil
import subprocess
import time
import pyautogui
from resources import *
from pynput.keyboard import Key, Controller  # 导入按键控制
import paramiko
from pojo import FolderSelection
from xhell import select_vm

# 创建一个键盘控制对象
KEYBOARD = Controller()
# 屏幕的长宽
WIDTH, HEIGHT = pyautogui.size()


def key_press_down(times, *key):
    """键盘按下键盘。接收一个可变参数。"""
    for k in key:
        KEYBOARD.press(k)
    time.sleep(times)
    for k in key:
        KEYBOARD.release(k)


def mouse_click(x=WIDTH/2, y=HEIGHT/2, button='left', times=0.1):
    """鼠标点击。默认点击中间位置，按下与抬起间隔为0.1秒。"""
    pyautogui.click(x=x, y=y, button=button)
    time.sleep(times)


def open_idea_and_run_project(idea_path):
    """打开idea"""
    subprocess.Popen([IDEA_EXT, idea_path])
    # todo 运行项目，可使用 Groovy 脚本
    # ......


def open_vm_and_run_project(vm_path):
    """运行vm并打开虚拟机"""

    # 打开vm，并打开虚拟机
    subprocess.Popen([VM_EXE, vm_path])
    time.sleep(10)
    # 键盘按下ctrl + b 并停顿0.5秒抬起，以运行虚拟机
    key_press_down(0.5, Key.ctrl, "b")
    """
    从这里应该已经结束，不过在vm中启动linux虚拟机需要鼠标点进去按下确定默认启动项，
    然后ctrl + alt 返回原窗口。下面的代码就是在做这样的一件事，但是有bug，
    print可以正常输出，但是动作没有效果，先放着，以后再说
    """
    time.sleep(2)
    # todo 虽然下面的print执行，但是在vm页面并没有具体的显示
    # 点击中心位置点击屏幕，以进入vm
    mouse_click()
    print("鼠标点击进入vm")
    # 跳过选择，并退出虚拟机界面
    key_press_down(0.1, Key.enter)
    key_press_down(0.1, Key.ctrl, Key.alt)
    print("光标退出vm...")


def open_xshell():
    """打开Xshell并连接vm"""
    subprocess.Popen(Xshell_EXE)
    time.sleep(5)
    # 调用模板匹配并选择虚拟机
    select_vm(TEMPLATE_PATH_VM)



def is_idea_running(exe_name):
    """检查程序否正在运行"""

    # 遍历所有进程，判断是否存在指定的进程名
    for proc in psutil.process_iter(['pid', 'name']):
        if exe_name in proc.info['name'].lower():
            return True
    return False


def check_log_for_completion(log_file_path, keyword):
    """检查日志文件是否包含指定的关键字"""

    # 检查文件是否存在
    if not os.path.exists(log_file_path):
        return False
    with open(log_file_path, 'r', encoding='utf-8') as log_file:
        # 循环检查日志文件的末尾部分是否包含项目加载完成的关键字
        lines = log_file.readlines()
        for line in lines:
            if keyword in line:
                return True
    return False


def reset_log_file(log_file_path):
    """清空日志文件，确保新的运行不会受到旧日志的影响"""
    if os.path.exists(log_file_path):
        open(log_file_path, 'w', encoding="utf-8").close()  # 清空文件内容


def check(exe_name, log_file_path, keyword):
    # 每隔几秒检查一次日志文件，直到项目加载完成
    while True:
        if is_idea_running(exe_name):
            if check_log_for_completion(log_file_path, keyword):
                print(exe_name + "完成加载")
                break
            else:
                print(exe_name + "项目正在加载...")
        else:
            print(exe_name + "没有在运行中...")
        time.sleep(5)


def check_ssh_connection(host, port=22, username='root', password='123456', timeout=5):
    """尝试通过 SSH 连接到虚拟机"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(host, port=port, username=username, password=password, timeout=timeout)
        return True
    except (paramiko.ssh_exception.NoValidConnectionsError, paramiko.ssh_exception.SSHException, TimeoutError) as e:
        print(f"SSH 连接失败: {e}")
        return False
    finally:
        ssh.close()


def check_vm_connection():
    while True:
        if check_ssh_connection(VM_IP):
            print("VM 已经完成启动...")
            break
        else:
            print("VM 正在尝试重试....")
        time.sleep(5)


def run_idea(idea_path):
    # 每次程序开始运行时清空日志
    reset_log_file(LOG_FILE_PATH_IDEA)
    # 启动 IDEA
    open_idea_and_run_project(idea_path)
    # 检查是否加载完成
    check('idea', LOG_FILE_PATH_IDEA, KEYWORD_IDEA)


def run_vm(vm_path):
    # 启动 VM 并打开虚拟机
    open_vm_and_run_project(vm_path)
    # 检查虚拟机是否完成启动
    check_vm_connection()


def run_xshell(pro_name):
    # 每次程序开始运行时清空日志
    reset_log_file(LOG_FILE_PATH_XSHELL)
    # 启动 XSHELL
    open_xshell()
    # 检查是否加载完成
    check('xshell', LOG_FILE_PATH_XSHELL, pro_name)


def run(folder_selections: list[FolderSelection]):

    """启动"""
    for item in folder_selections:
        if item.get_software() == "IDEA":
            run_idea(item.get_path())
        elif item.get_software() == "VMware":
            run_vm(item.get_path())
        elif item.get_software() == "XShell":
            run_xshell(item.get_pro_name())








