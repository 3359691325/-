#!/user/bin/env python3
# -*- coding = utf-8 -*-
_author_ = 'tq'
from tkinter import *
from tkinter import messagebox

import addmain
import shanmain
import shuchu


class zhumain():
    def __init__(self):
        # 定义一个更新公告
        self.p = '''
        当前版本：v1.3
        更新日志：
            v1.1 添加账号登录系统（并增加用户权限）
            v1.2 修复登录界面随意输密码登录
            v1.3 添加更新日志
            v1.4 使用分散的类来进行构架，增加运行速度并且便于修改代码
                '''
        self.zhu = Tk()
        self.zhu.title('管理系统')
        self.zhu.geometry('700x550')
        self.label = Label(self.zhu, text='管理系统', bg='pink')
        self.button = Button(self.zhu, text='添加学生信息', height=2, command=self.add)
        self.button1 = Button(self.zhu, text='删除学生信息', height=2, command=self.shan)
        self.button2 = Button(self.zhu, text='输出学生信息', height=2, command=self.shuchu)
        self.button3 = Button(self.zhu, text='   退出系统   ', height=2, command=self.exit)
        self.t = Text(self.zhu)

    def zhu1(self):
        self.button.place(height=40, width=80, x=10, y=10)
        self.button1.place(height=40, width=80, x=10, y=60)
        self.button2.place(height=40, width=80, x=10, y=110)
        self.button3.place(height=40, width=80, x=10, y=160)
        self.t.place(height=300, width=680, x=10, y=210)
        # print(v)
        # 进行判断权限
        # 为1则为超级管理员 为2则为管理员
        # 两种账号功能不相同
        if v == 1:
            c = '当前用户 %s\n权限 超级管理员'
        else:
            c = '当前用户 %s\n权限 管理员'
        self.t.insert('insert', c % b)
        self.t.insert('insert', self.p)

    # 跳转页面
    def add(self):
        if v == 0:
            messagebox.showinfo(title='错误', message='您没有权限使用此功能')
        else:
            addmain.main()

    def shan(self):
        if v == 0:
            messagebox.showinfo(title='错误', message='您没有权限使用此功能')
        else:
            shanmain.main()

    def shuchu(self):
        shuchu.main()

    def exit(self):
        self.zhu.destroy()


def main(v1, b1):
    global b
    b = v1
    global v
    v = b1
    ma = zhumain()
    ma.zhu1()
    mainloop()
