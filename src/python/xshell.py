# ======= File: xshell.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/8 19:51
# @Desc : Xshell 中如何利用图像识别选择连接哪个虚拟机

import cv2
import pyautogui
import numpy as np
from PIL import ImageGrab
import time


# 截取当前屏幕
def screenshot():
    screen = ImageGrab.grab()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)  # 转换为灰度图像
    return screen_gray


# 模板匹配
def find_template_on_screen(template_path):
    screen_gray = screenshot()

    # 读取模板图片
    template = cv2.imread(template_path, 0)

    # 使用模板匹配，找到模板在屏幕上的位置
    res = cv2.matchTemplate(screen_gray, template, cv2.TM_CCOEFF_NORMED)

    # 设定一个匹配的阈值，通常为 0.8 或以上
    threshold = 0.8
    loc = np.where(res >= threshold)

    # 如果找到匹配位置，返回第一个匹配的点
    if len(loc[0]) > 0:
        return loc[1][0], loc[0][0]
    else:
        return None


# 自动化选择虚拟机的流程
def select_vm(template_path):
    # 等待 Xshell 打开
    time.sleep(2)

    # 查找虚拟机名称所在的位置
    pos = find_template_on_screen(template_path)

    if pos:
        # 将鼠标移动到虚拟机名称位置，并点击
        x, y = pos
        pyautogui.moveTo(x + 10, y + 10)  # 防止点击到边缘，适当偏移
        pyautogui.click()

        # 模拟回车连接虚拟机
        time.sleep(1)
        pyautogui.press('enter')
    else:
        print("没有找到虚拟机名称的匹配位置。")

# 调用模板匹配并选择虚拟机
# select_vm('../photoes/vm.jpg')