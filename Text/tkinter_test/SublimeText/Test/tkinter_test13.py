import os
import tkinter
from tkinter import Tk, Menu, Text, filedialog, messagebox


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
        file_menu.add_command(label='Test', command = self.read)
        menu_bar.add_cascade(label='File', menu = file_menu)


        #编辑
        edit_menu = Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label = '撤销',accelerator = 'ctrl + z')
        edit_menu.add_command(label = '重做',accelerator = 'ctrl + y')
        edit_menu.add_command(label = '复制',accelerator = 'ctrl + c')
        edit_menu.add_command(label = '剪切',accelerator = 'ctrl + x')
        edit_menu.add_command(label = '粘贴',accelerator = 'ctrl + v')
        edit_menu.add_command(label = '查找',accelerator = 'ctrl + F')
        edit_menu.add_command(label = '全选',accelerator = 'ctrl + A')
        menu_bar.add_cascade(label='Edit', menu=edit_menu)

        #关于
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label = '作者')
        help_menu.add_command(label = '版权')
        menu_bar.add_cascade(label='Help', menu=help_menu)

        self.src_filename = None
        self.text_area = Text()
        self.text_area.pack()
        win.mainloop()

    def new_file(self):
        data = self.read()
        save_flag = False
        if data and messagebox.askokcancel('提示', '当前内容要进行保存吗？'):
            if self.src_filename:
                self.sava_file(self.src_filename)
                save_flag = True
            else:
                new_filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
                if new_filename:
                    self.sava_file(new_filename)
                    save_flag = True
        if save_flag:
            self.clear()

    def open_file(self):
        self.new_file()
        # 获取文件名
        self.src_filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])
        if self.src_filename:
            # 获取数据
            data = open(self.src_filename).read()
            # 填充到text控件
            self.text_area.insert(tkinter.INSERT, data)

    # 保存文件
    def save_file(self):
        self.save(self.src_filename)

    # 另存为
    def save_as_file(self):
        self.save(None)

    # 文件存在，直接替换；文件不存在，创建文件，直接写入
    def save(self, filename):
        # 打开-保存
        if filename:
            pass
        # 新建-保存， 更改-保存， 另存为
        else:
            filename = filedialog.askopenfilename(filetypes=[('txt格式', 'txt')])

            filedialog.askopenfile()
            filedialog.ask
            print('filename:', filename)
        if filename:
            path = os.path.dirname(filename+'txt')
            if not os.path.exists(path):
                os.makedirs(path)
            with open(filename, 'w') as f:
                f.write(self.read())
            messagebox.showinfo('提示', '保存成功')

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





