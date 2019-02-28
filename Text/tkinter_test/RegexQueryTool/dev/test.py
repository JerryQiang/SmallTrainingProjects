from tkinter import *

'''
1、这个程序实现文本框输入。
2、使用grid方法按照Excel表格方式对组件位置进行安排
3、通过Button提交按钮实现获取用户的输入信息。
'''
root = Tk()

Label1 = Label(root, text='会员名称:').grid(row=0, column=0)
Label2 = Label(root, text='会员代号:').grid(row=1, column=0)
print(Label(root, text='会员名称:').grid(row=0, column=0))
print(Label(root, text='会员代号:').grid(row=1, column=0))

v1 = StringVar()
p1 = StringVar()
e1 = Entry(root, textvariable=v1)  # Entry 是 Tkinter 用来接收字符串等输入的控件.
e2 = Entry(root, textvariable=p1, show='#')
e1.grid(row=0, column=1, padx=10, pady=5)  # 设置输入框显示的位置，以及长和宽属性
e2.grid(row=1, column=1, padx=10, pady=5)


def show():
    print("会员名称:%s" % e1.get())  # 获取用户输入的信息
    print("会员代号:%s" % e2.get())


Button(root, text='验证信息', width=10, command=show) \
    .grid(row=2, column=0, sticky=W, padx=10, pady=5)

Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=2, column=1, sticky=E, padx=10, pady=5)

mainloop()