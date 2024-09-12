# ======= File: main.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/6 13:27
# @Desc : 主函数

import tkinter as tk
from pojo import App


if __name__ == "__main__":
    # 主程序
    root = tk.Tk()
    app = App(root)
    root.geometry("1000x500")
    root.mainloop()
