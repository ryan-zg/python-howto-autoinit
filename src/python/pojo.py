# ======= File: pojo.py =======

# -*- coding: utf-8 -*-
# @Author : Ryan Zhang
# @Date : 2024/9/11 20:09
# @Desc : there need something...

class FolderSelection:
    def __init__(self, path='', software='', pro_name=""):
        self.path = path
        self.software = software
        self.pro_name = pro_name

    def get_path(self):
        return self.path.get()

    def get_software(self):
        return self.software.get()

    def get_pro_name(self):
        return self.pro_name.get()

    def __str__(self):
        return f"{self.get_path()},{self.get_software()},{self.get_pro_name()}"
