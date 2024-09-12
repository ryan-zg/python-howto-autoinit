# ======= File: pojo.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/11 20:09
# @Desc : there need something...

from tkinter import filedialog, ttk
import json
import os
from resources import SOFTWARE_ARR, JSON_FILE_PATH
from method import run
import tkinter as tk


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("自动打开软件")

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        # 提示信息
        self.label = tk.Label(self.frame, text="请选择文件或文件夹并配置软件打开方式：")
        self.label.grid(row=0, column=0, columnspan=5)

        # 列表，存储动态添加的行
        self.row_list = []

        # 添加按钮
        self.add_button = tk.Button(self.frame, text="添加", command=self.add_row)
        self.add_button.grid(row=1, column=0, pady=5)

        # 删除按钮
        self.remove_button = tk.Button(self.frame, text="删除", command=self.remove_row)
        self.remove_button.grid(row=1, column=1, pady=5)

        # 确定按钮
        self.confirm_button = tk.Button(self.frame, text="确定", command=self.confirm)
        self.confirm_button.grid(row=1, column=2, pady=5)

        # 读取持久化的配置
        self.load_config()

    def add_row(self, data=None):
        row_index = len(self.row_list) + 2  # 行号，预留给上面的控件

        # 选择文件还是文件夹的下拉框
        select_type_combo = ttk.Combobox(self.frame, values=["文件", "文件夹"], width=10)
        select_type_combo.grid(row=row_index, column=0)
        select_type_combo.current(0)  # 默认选择文件

        # 选择文件/文件夹按钮
        select_button = tk.Button(self.frame, text="选择", command=lambda: self.select_path(row_index - 2))
        select_button.grid(row=row_index, column=1)

        # 显示文件路径的输入框
        path_entry = tk.Entry(self.frame, width=30)
        path_entry.grid(row=row_index, column=2)

        # 软件选择下拉框
        software_combo = ttk.Combobox(self.frame, values=SOFTWARE_ARR, width=10)
        software_combo.grid(row=row_index, column=3)

        # 额外信息输入框
        info_entry = tk.Entry(self.frame, width=20)
        info_entry.grid(row=row_index, column=4)

        # 如果传入了数据（从持久化文件读取的），则加载到界面中
        if data:
            select_type_combo.set(data['select_type'])
            path_entry.insert(0, data['path'])
            software_combo.set(data['software'])
            info_entry.insert(0, data['pro_name'])

        # 将这一行的控件打包存入 row_list
        self.row_list.append((select_type_combo, select_button, path_entry, software_combo, info_entry))

    def remove_row(self):
        if self.row_list:
            last_row = self.row_list.pop()

            for widget in last_row:
                widget.grid_forget()  # 删除行中的每个控件

    def select_path(self, index):
        select_type = self.row_list[index][0].get()  # 获取选择的是文件还是文件夹

        if select_type == "文件":
            file_selected = filedialog.askopenfilename()  # 打开文件选择对话框
        else:
            file_selected = filedialog.askdirectory()  # 打开文件夹选择对话框

        if file_selected:
            self.row_list[index][2].delete(0, tk.END)  # 清空文本框
            self.row_list[index][2].insert(0, file_selected)  # 插入选择的文件或文件夹路径

    def confirm(self):
        # 收集所有行中的数据，并保存到文件中
        data = []
        for row in self.row_list:
            row_data = {
                'select_type': row[0].get(),
                'path': row[2].get(),
                'software': row[3].get(),
                'pro_name': row[4].get()
            }
            data.append(row_data)
            # print(f"选择类型: {row_data['select_type']}, 路径: {row_data['path']}, 软件: {row_data['software']}, 额外信息: {row_data['pro_name']}")
        run(data)
        # 持久化数据到文件
        self.save_config(data)

    def save_config(self, data):
        with open(JSON_FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_config(self):
        # 读取持久化的配置文件
        if os.path.exists(JSON_FILE_PATH):
            with open(JSON_FILE_PATH, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 根据持久化的数据加载界面
            for row_data in data:
                self.add_row(row_data)