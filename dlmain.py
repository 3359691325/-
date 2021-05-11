#!/user/bin/env python3
# -*- coding = utf-8 -*-
_author_ = 'tq'
from tkinter import *
from tkinter import messagebox

import pymysql

import zhumain

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'dt78'
}


class dlmain():
    def denglu1(self):
        # print("jfajiofa")
        # 登录验证，通过登录来获取用户的权限

        cc = self.denglu.cursor()

        global v
        v = 0
        global b1
        b1 = ''
        b = '''
        select * from admin where username = %s
               '''
        c = '''
        select * from admin where pd = %s
              '''
        name = self.name1.get()
        pd = self.pd1.get()
        if len(name) <= 0 or len(pd) <= 0:
            messagebox.showinfo(title='错误', message='请不要留空')
        else:
            cc.execute(b, name)
            b1 = cc.fetchall()
            if len(b1) <= 0:
                messagebox.showinfo(title='错误', message='用户名不存在')
            else:
                for c in b1:
                    self.nameyz = c[1]
                if self.nameyz != pd:
                    messagebox.showinfo(title='错误', message='密码输入错误')
                else:

                    # cc.execute(c, pd)
                    # b2 = cc.fetchall()
                    # if len(b2) <= 0:
                    #     messagebox.showinfo(title='错误', message='密码输入错误')
                    # else:
                    messagebox.showinfo(title='成功', message='登录成功')
                    # 登录成功时获取权限 为1则为超级管理员，为2则为管理员 管理员只能进行查询 不能添加用户和删除用户
                    for i in b1:
                        v = i[2]
                    b = name
                    self.dl.destroy()
                    zhumain.main(b, v)

    def __init__(self):
        self.denglu = pymysql.connect(**config)
        self.nameyz = ''
        self.dl = Tk()
        self.dl.title("登录页面")
        self.dl.geometry('700x500')
        self.name = Label(self.dl, text='      用户名')
        self.pd = Label(self.dl, text='     密码')
        self.name1 = Entry(self.dl)
        self.pd1 = Entry(self.dl)
        self.deng = Button(self.dl, text='登录', command=self.denglu1)

    def ckxs(self):
        self.name.place(height=50, width=80, x=300, y=2)
        self.name1.place(height=30, width=200, x=250, y=40)
        self.pd.place(height=50, width=80, x=300, y=80)
        self.pd1.place(height=30, width=200, x=250, y=128)
        self.deng.place(height=30, width=100, x=300, y=200)


def main1():
    ma = dlmain()
    ma.ckxs()
    mainloop()


if __name__ == '__main__':
    main1()
