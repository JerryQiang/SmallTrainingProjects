import os
import hashlib
import tkinter
from tkinter import Tk, Menu, filedialog, messagebox,Text

# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Post it Notes Program(5.文本编辑器) 记事本类型的应用
可以打开、编辑、保存文本文档。
可以增加单词高亮和其它的一些特性。

'''


# 单页面文本记事本
class SublimeText():
    def __init__(self):
        self.win = Tk()  # 生成win主窗口
        self.win.title('Simulate Sublime Text')
        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)  # 去除虚线框
        file_menu.add_command(label='New File', accelerator='Ctrl+N', command=self.new_file)
        file_menu.add_command(label='Open File...', accelerator='Ctrl+O', command=self.open_file)
        file_menu.add_command(label='Save', accelerator='Ctrl+S', command=self.save_file)
        file_menu.add_command(label='Save As...', accelerator='Ctrl+Shift+S', command=self.save_as_file)
        file_menu.add_separator()  # 菜单选项栏增添横线
        file_menu.add_command(label='Exit', command=self.exit_file)
        menu_bar.add_cascade(label='File', menu = file_menu)


        file_menu.bind_all('<Control-n>', lambda event:self.new_file())
        file_menu.bind_all('<Control-o>', lambda event:self.open_file())
        file_menu.bind_all('<Control-s>', lambda event: self.save_file())
        file_menu.bind_all('<Control-S>', lambda event: self.save_file())

        # 创建编辑菜单
        edit_menu = Menu(menu_bar, tearoff=False)

        # 创建编辑下拉内容
        edit_menu.add_command(label="Undo", accelerator='Ctrl+Z', command=self.undo_opr)
        edit_menu.add_separator()
        edit_menu.add_command(label="Copy", accelerator='Ctrl+C', command=self.copy_opr)
        edit_menu.add_command(label="Cut", accelerator='Ctrl+X', command=self.cut_opr)
        edit_menu.add_command(label="Paste", accelerator='Ctrl+V', command=self.paste_opr)
        menu_bar.add_cascade(label='Edit', menu=edit_menu)

        edit_menu.bind_all('<Control-z>', lambda event: self.undo_opr())
        edit_menu.bind_all('<Control-c>', lambda event: self.copy_opr())
        edit_menu.bind_all('<Control-x>', lambda event: self.cut_opr())
        edit_menu.bind_all('<Control-v>', lambda event: self.paste_opr())

        # 创建帮助菜单
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About Sublime Text', command=self.about_msg)
        menu_bar.add_cascade(label='Help', menu=help_menu)

        self.src_filename = None
        self.text_area = Text()
        self.cd_key = None
        self.text_area.pack()

        self.win.mainloop()

    # 新建文件
    def new_file(self):
        self.save_file()
        self.clear()

    # 打开文件
    def open_file(self):
        self.save_file()
        src_dir, src_filename = self.default_dir_and_file()
        filename = filedialog.askopenfilename(initialdir=src_dir, initialfile=src_filename, filetypes=[('txt格式', 'txt')])
        if filename is not None and os.path.exists(filename):
            file = open(filename, 'r')
            cnt = file.read()
            self.write(cnt)
            self.update_cd_key()

    # 保存文件
    def save_file(self):
        # 新建文件
        if self.src_filename is None:
            # 对内容为空字符串组合不予保存
            if self.read() != '':
                self.save_as_file()
        # 打开文件
        else:
            # 文件改变 且 保存当前内容
            if self.is_changed() and messagebox.askokcancel('提示', '当前内容要进行保存吗？'):
                file = open(self.src_filename, 'w')
                file.write(self.read())
                self.update_cd_key()

    # 另存为
    def save_as_file(self):
        # 默认路径，文件名
        src_dir, src_filename = self.default_dir_and_file()
        filename = filedialog.asksaveasfilename(initialdir=src_dir, initialfile=src_filename, filetypes=[('txt格式', 'txt')])
        if filename is not None and os.path.exists(filename):
            file = open(filename, 'w')
            file.write(self.read())
            self.update_cd_key()

    # 退出
    def exit_file(self):
        self.save_file()
        self.win.quit()

    def undo_opr(self):
        self.text_area.edit_undo()

    # 复制功能函数
    def copy_opr(self):
        global content
        content = self.text_area.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        return content

    # 剪切函数
    def cut_opr(self):
        global content

        content = self.text_area.get(tkinter.SEL_FIRST, tkinter.SEL_LAST)
        self.text_area.delete(tkinter.SEL_FIRST, tkinter.SEL_LAST)

        return content

    # 粘贴功能函数
    def paste_opr(self):
        self.text_area.insert(tkinter.INSERT, content)

    def about_msg(self):
        messagebox.showinfo("Sublime Text", "Sublime Text\n开发者：蒋志强\n联系方式：1131233593@qq.com\nCopyright © 2019 Version3.0")

    # 默认路径，文件名
    def default_dir_and_file(self):
        # 桌面路径:os.path.join(os.path.expanduser("~"), 'Desktop')
        src_dir, src_filename = (os.path.join(os.path.expanduser("~"), 'Desktop'), '')
        if self.src_filename is not None:
            src_dir, src_filename = os.path.split(self.src_filename)
        return src_dir, src_filename

    # md5_cd_key记录文件内容
    def md5_cd_key(self, s):
        md5 = hashlib.md5(s.encode('utf-8'))
        return md5.hexdigest()

    def update_cd_key(self):
        self.cd_key = self.md5_cd_key(self.read())

    def is_changed(self):
        return self.cd_key != self.md5_cd_key(self.read())

    def read(self):
        return self.text_area.get(1.0, tkinter.END).strip()

    def clear(self):
        self.text_area.delete(1.0, tkinter.END)

    def write(self, data):
        self.clear()
        self.text_area.insert(tkinter.INSERT, data)


if __name__ == '__main__':
    sublime_text = SublimeText()





