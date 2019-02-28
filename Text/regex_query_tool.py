import re
from tkinter import *

'''
1、这个程序实现文本框输入。
2、使用grid方法按照Excel表格方式对组件位置进行安排
3、通过Button提交按钮实现获取用户的输入信息。
'''
class RegexQueryTool:
    def __init__(self):

        self.root = Tk()
        self.root.title('正则查询工具')
        self.Label1 = Label(self.root, text='字符串:')
        self.Label1.grid(row=0, column=0)
        self.Label2 = Label(self.root, text='正则表达式:')
        self.Label2.grid(row=1, column=0)
        self.Label3 = Label(self.root, text='匹配结果:')
        self.Label3.grid(row=2, column=0)
        self.Label4 = Label(self.root, text='')
        self.Label4.grid(row=2, column=1)


        self.v1 = StringVar()
        self.p1 = StringVar()
        self.e1 = Entry(self.root, textvariable=self.v1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
        self.e2 = Entry(self.root, textvariable=self.p1)
        self.e1.grid(row=0, column=1, padx=10, pady=5)  # 设置输入框显示的位置，以及长和宽属性
        self.e2.grid(row=1, column=1, padx=10, pady=5)

        Button(self.root, text='验证信息', width=10, command=self.show) \
            .grid(row=3, column=0, sticky=W, padx=10, pady=5)

        Button(self.root, text='退出', width=10, command=self.root.quit) \
            .grid(row=3, column=1, sticky=E, padx=10, pady=5)
        self.root.mainloop()

    def show(self):
        string = self.e1.get()
        regex = self.e2.get()
        # print("字符串:%s" % string)  # 获取用户输入的信息
        # print("正则表达式:%s" % regex)
        res = re.match(regex, string).group()
        # print(res)
        self.Label4['text'] = res
        return re.findall(regex, string)

if __name__ == '__main__':
    RegexQueryTool()


