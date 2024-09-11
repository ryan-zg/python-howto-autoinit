# ======= File: main.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/6 13:27
# @Desc : 主函数

from method import run
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from pojo import FolderSelection
import json


if __name__ == "__main__":
    """程序启动项"""

    file_path = "./info.json"

    root = tk.Tk()
    root.title("文件夹选择示例")

    # 设置窗口大小
    root.geometry("1500x500")

    # 存储所有文件夹和软件选择
    folder_selections: list[FolderSelection] = []

    SOFTWARE_ARR = ['IDEA', 'VMware', 'XShell']

    # 动态添加输入框、选择按钮和下拉框
    def add_folder_row():
        global row_index
        row_index += 1

        # 添加输入框
        entry = tk.Entry(root, width=50)
        entry.grid(row=row_index, column=0, padx=10, pady=10)

        # 定义选择文件夹的函数
        def choose_directory():
            directory_path = filedialog.askdirectory()
            entry.delete(0, tk.END)
            entry.insert(0, directory_path)

        # 选择文件
        def choose_file():
            directory_path = filedialog.askopenfilename()
            entry.delete(0, tk.END)
            entry.insert(0, directory_path)

        # 添加选择文件夹的按钮
        button = tk.Button(root, text="选择文件夹", command=choose_directory)
        button.grid(row=row_index, column=1, padx=5, pady=10)

        # 添加选择文件的按钮
        button = tk.Button(root, text="选择文件", command=choose_file)
        button.grid(row=row_index, column=2, padx=5, pady=10)

        # 添加下拉框
        software_var = tk.StringVar(value="选择软件")
        software_combobox = ttk.Combobox(root, textvariable=software_var, values=SOFTWARE_ARR, width=10)
        software_combobox.grid(row=row_index, column=3, padx=10, pady=10)

        # 添加输入框
        text_combox = tk.Entry(root, width=10)
        text_combox.grid(row=row_index, column=4, padx=10, pady=10)

        # 将组件保存到列表中
        folder_selections.append(FolderSelection(entry, software_combobox, text_combox))

    # 输出所有路径和软件选择
    def output_paths_and_software():

        # run(folder_selections)
        # 删除文件中的信息
        open(r'./info.json', 'w', encoding="utf-8").close()
        # 将数据写入文件
        selections_data = []
        for selection in folder_selections:
            selections_data.append({
                'path': selection.get_path(),
                'software': selection.get_software(),
                'pro_name': selection.get_pro_name()
            })
        with open(file_path, 'w') as file:
            json.dump(selections_data, file)


    row_index = 3
    try:
        with open(file_path, 'r') as file:

            selections = json.load(file)
            for selection in selections:

                path_entry = tk.Entry(root, width=50)
                path_entry.insert(0, selection['path'])
                path_entry.grid(row=row_index, column=0, padx=10, pady=10)
                def choose_directory():
                    directory_path = filedialog.askdirectory()
                    path_entry.delete(0, tk.END)
                    path_entry.insert(0, directory_path)
                def choose_file():
                    directory_path = filedialog.askopenfilename()
                    path_entry.delete(0, tk.END)
                    path_entry.insert(0, directory_path)
                    # 添加选择文件夹的按钮

                button = tk.Button(root, text="选择文件夹", command=choose_directory)
                button.grid(row=row_index, column=1, padx=5, pady=10)

                # 添加选择文件的按钮
                button = tk.Button(root, text="选择文件", command=choose_file)
                button.grid(row=row_index, column=2, padx=5, pady=10)

                # todo 循环中值被覆盖
                software_var = tk.StringVar(value=selection['software'])
                software_combobox = ttk.Combobox(root, textvariable=software_var, values=SOFTWARE_ARR, width=10)
                software_combobox.grid(row=row_index, column=3, padx=10, pady=10)

                pro_name_entry = tk.Entry(root, width=10)
                pro_name_entry.insert(0, selection['pro_name'])
                pro_name_entry.grid(row=row_index, column=4, padx=10, pady=10)

                folder_selections.append(FolderSelection(path_entry, software_combobox, pro_name_entry))

                row_index += 1
    except FileNotFoundError:
        pass


    # 添加一个标签
    label1 = tk.Label(root, text="选择要打开的项目文件夹路径, 选择要开启的软件, 选择要连接的虚拟机名称(XShell等需要, 可以不填)")
    label1.grid(row=0, column=0, columnspan=2, pady=10)
    # 添加一个标签
    label2 = tk.Label(root, text="添加文件夹的顺序即为打开软件的顺序，请注意选择，例如 VMware 应该在 Xshell 之前。区分文件夹还是文件，比如VMware要打开vmx文件")
    label2.grid(row=1, column=0, columnspan=2, pady=5)
    # 添加一个标签
    label3 = tk.Label(root, text="VMware文件夹例子：D:/XXXX/XXXX.vmx。输入框没有可以不填，例如XShell只需填后两个")
    label3.grid(row=2, column=0, columnspan=2, pady=5)

    # 添加一个“添加文件夹”的按钮
    add_button = tk.Button(root, text="添加文件夹", command=add_folder_row)
    add_button.grid(row=3, column=5, padx=10, pady=10)

    # 添加一个“确认”按钮
    confirm_button = tk.Button(root, text="确认", command=output_paths_and_software)
    confirm_button.grid(row=3, column=6, columnspan=3, pady=15)

    # 进入消息循环
    root.mainloop()
