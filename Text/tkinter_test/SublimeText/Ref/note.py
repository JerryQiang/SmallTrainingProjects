# !/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Post it Notes Program(5.文本编辑器) 记事本类型的应用
可以打开、编辑、保存文本文档。
可以增加单词高亮和其它的一些特性。

'''

"""
    1）页面布局
    2）基本文本编辑功能，增删改查替
    3）编码选择
    4）大小写，url编码
    5）新建
    6）打开
    7）保存/另存为
"""

# GUI界面编程
from tkinter import *  # 控件基础包，导入这个包后，这个包下的所有函数可以直接调用
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from urllib.parse import quote


class MainWin():
    # 顶层窗口
    def __init__(self):
        top_button_width = 10
        button_relief = RAISED

        # 创建顶层窗口
        root = Tk()
        self.src_filename = None
        self.count = StringVar()
        self.count.set('0')
        # root.geometry(str(win_width)+'x750')  # 初始化窗口大小
        root.title('简易的文本记事器')
        # 宽不可变, 高可变,默认为True
        root.resizable(width=False, height=False)

        # 上部控件
        Button(root, text='打开', relief=button_relief, width=top_button_width, command=self.open_button_event) \
            .grid(row=0, column=0)
        Button(root, text='新建', relief=button_relief, width=top_button_width, command=self.new_button_event) \
            .grid(row=0, column=1)
        Button(root, text='保存', relief=button_relief, width=top_button_width,
               command=self.new_button_event).grid(row=0, column=2, sticky=E)
        Button(root, text='另存为', relief=button_relief, width=top_button_width,
               command=self.other_save_button_event).grid(row=0, column=3, sticky=W)
        Button(root, text='关于作者', bg='SkyBlue', font='Arial', width=top_button_width, command=self.help_author).grid(
            row=0, column=7, sticky=E)

        # 隔开一行
        Label(root, text='').grid(row=1)

        # 中部控件
        Button(root, text='查找', relief=button_relief, width=top_button_width, command=self.find_button_event) \
            .grid(row=2, column=0, sticky=N)
        self.find_text = Text(root, width=top_button_width, height=2)
        self.find_text.grid(row=2, column=1)
        Label(root, text='查找总数').grid(row=3, column=0, sticky=N)
        self.count_label = Label(root, textvariable=self.count)
        self.count_label.grid(row=3, column=1)

        Button(root, text='替换成', relief=button_relief, width=top_button_width, command=self.replace_button_event).grid(
            row=4, column=0, sticky=N)
        self.replace_text = Text(root, width=top_button_width, height=2)
        self.replace_text.grid(row=4, column=1, sticky=N)

        Button(root, text='大写', relief=button_relief, width=top_button_width, command=self.upper_button_event).grid(
            row=5, column=0, sticky=N)
        Button(root, text='小写', relief=button_relief, width=top_button_width, command=self.lower_button_event).grid(
            row=5, column=1, sticky=N)

        Button(root, text='编码选择', relief=button_relief, width=top_button_width,
               command=self.code_change_button_event).grid(row=6, column=0, sticky=N)
        self.code_chosen = Combobox(root, width=top_button_width - 2)
        self.code_chosen['values'] = ('utf-8', 'gb2312', 'gbk')
        self.code_chosen.grid(row=6, column=1)

        Button(root, text='URL编码', relief=button_relief, width=top_button_width,
               command=self.url_encode_button_event).grid(row=7, column=0, sticky=N)

        self.text = Text(root)
        self.text.grid(row=2, column=2, columnspan=6, rowspan=15)

    def open_button_event(self):
        self.new_button_event()
        # 获取文件名
        self.src_filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if self.src_filename:
            # 获取数据
            data = open(self.src_filename).read()
            # 填充到text控件
            self.text.insert(INSERT, data)

    def new_button_event(self):
        data = self.__get()
        save_flag = False
        if data and messagebox.askokcancel('提示', '当前内容要进行保存吗？'):
            if self.src_filename:
                self.__sava_data(self.src_filename)
                save_flag = True
            else:
                new_filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
                if new_filename:
                    self.__sava_data(new_filename)
                    save_flag = True
        if save_flag:
            self.text.delete(1.0, END)

    def save_button_event(self):
        filename = self.src_filename if self.src_filename else filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if filename:
            self.__sava_data(filename)

    def other_save_button_event(self):
        filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if filename:
            self.__sava_data(filename)

    def find_button_event(self):
        data = self.__get()
        find_data = self.find_text.get(1.0, END).strip()
        if find_data not in data:
            messagebox.showinfo('提示', '搜索的字符不存在')
        else:
            self.count.set(str(data.count(find_data)))

    def replace_button_event(self):
        find_data = self.find_text.get(1.0, END).strip()
        replace_data = self.replace_text.get(1.0, END).strip()
        data = self.__get()
        data = data.replace(find_data, replace_data)
        self.__del_and_set(data)

    def code_change_button_event(self):
        try:
            data = self.__get().encode(self.code_chosen.get().strip())
        except:
            messagebox.showinfo('提示', '无法进行编码')
        else:
            self.__del_and_set(data)

    def url_encode_button_event(self):
        data = '\n' * 2 + '*' * 20 + '以下是URL编码' + '*' * 20 + '\n' + quote(self.__get(), 'utf-8')
        self.text.see(END)
        self.text.insert(END, data)

    def upper_button_event(self):
        data = self.__get().upper()
        self.__del_and_set(data)

    def lower_button_event(self):
        data = self.__get().lower()
        self.__del_and_set(data)

    def help_author(self):
        messagebox.showinfo('关于作者', '作者：MADAO程序猿 \nQQ：1506795308')

    def __sava_data(self, filename):
        with open(filename, 'w') as f:
            f.write(self.__get())
        messagebox.showinfo('提示', '保存成功')

    def __get(self):
        # 这里注意一定要有strip
        return self.text.get(1.0, END).strip()

    def __del_and_set(self, data):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, data)


main = MainWin()
mainloop()  # 运行这个GUI应用
