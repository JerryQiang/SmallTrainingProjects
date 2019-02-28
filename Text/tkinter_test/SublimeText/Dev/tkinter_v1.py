import os
import hashlib
import tkinter
from tkinter import Tk, Menu, Text, filedialog, messagebox


# 单文本记事本
class SublimeText():
    def __init__(self):
        win = Tk()  # 生成win主窗口
        win.title('Simulate Sublime Text')
        menu_bar = Menu(win)
        win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)  # 去除虚线框
        file_menu.add_command(label='New File', accelerator='Ctrl+N')
        file_menu.add_command(label='Open File...', accelerator='Ctrl+O')
        file_menu.add_command(label='Save', accelerator ='Ctrl+S', command=self.save_file)
        file_menu.add_command(label='Save As...', accelerator ='Ctrl+Shift+S', command=self.save_as_file)
        file_menu.add_separator()  # 菜单选项栏增添横线
        file_menu.add_command(label='Exit')
        file_menu.add_command(label='Test', command = self.test)
        menu_bar.add_cascade(label='File', menu = file_menu)

        self.src_filename = None
        self.text_area = Text()
        self.cd_key = None
        self.text_area.pack()

        win.mainloop()

    # 保存文件
    def save_file(self):
        # 文件是否新建
        if self.src_filename is None:
            self.save_as_file()
        else:
            # 文件改变 且 保存当前内容
            if self.is_changed() and messagebox.askokcancel('提示', '当前内容要进行保存吗？'):
                file = open(self.src_filename, 'w')
                file.write(self.read())

    # 另存为
    def save_as_file(self):
        # 默认路径，文件名
        src_dir, src_filename = self.default_dir_and_file()
        filename = filedialog.asksaveasfilename(initialdir=src_dir, initialfile=src_filename, filetypes=[('txt格式', 'txt')])
        if filename is not None:
            file = open(filename, 'w')
            file.write(self.read())

    # 默认路径，文件名
    def default_dir_and_file(self):
        src_dir, src_filename = (os.path.join(os.path.expanduser("~"), 'Desktop'), '*.txt')
        if self.src_filename is not None:
            src_dir, src_filename = os.path.split(self.src_filename)
        return (src_dir, src_filename)

    # md5_cd_key记录文件内容
    def md5_cd_key(s):
        md5 = hashlib.md5(s.encode('utf-8'))
        return md5.hexdigest()

    def is_changed(self):
        return self.cd_key!=self.md5_cd_key()

    def test(self):
        # filename = filedialog.askopenfile()
        # print(filename, type(filename))
        # filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        file = filedialog.asksaveasfile(initialfile='*.txt',filetypes=[('txt格式', 'txt')])
        print(file)
        file.write("猪年大吉")
        # filename = filedialog.asksaveasfilename(filetypes=[('txt格式', 'txt')])
        # f = open(filename, 'w')
        # print(f)
        # f.write('猪年大吉')
        # print(filename, type(filename))


    def read(self):
        print(self.text_area.get(1.0, tkinter.END).strip())
        return self.text_area.get(1.0, tkinter.END).strip()

    def clear(self):
        self.text_area.delete(1.0, tkinter.END)

    def write(self, data):
        self.clear()
        self.text_area.insert(tkinter.INSERT, data)


if __name__ == '__main__':
    sublime_text = SublimeText()





