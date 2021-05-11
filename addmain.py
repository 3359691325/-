#!/user/bin/env python3
# -*- coding = utf-8 -*-
_author_ = 'tq'
from tkinter import *
from tkinter import messagebox

import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'dt78'
}


class zhumain():
    def __init__(self):
        self.add = Tk()
        self.add.title('添加学生信息')
        self.add.geometry('500x350')
        self.label1 = Label(self.add, text='姓名')
        self.label2 = Label(self.add, text='年龄')
        self.label3 = Label(self.add, text='性别')
        self.entry1 = Entry(self.add)
        self.entry2 = Entry(self.add)
        self.entry3 = Entry(self.add)
        self.button1 = Button(self.add, text='提交数据', command=self.addshuju)

    def zhumain1(self):
        self.label1.pack()
        self.entry1.pack()
        self.label2.pack()
        self.entry2.pack()
        self.label3.pack()
        self.entry3.pack()
        self.button1.pack()

    def addshuju(self):
        lj = pymysql.connect(**config)
        abb = '''
insert into student
            (stu_name,stu_age,stu_sex)
        values
            (%s,%s,%s)
            '''
        name = self.entry1.get()
        age = self.entry2.get()
        sex = self.entry3.get()
        if len(name) == 0:
            messagebox.showinfo('错误', '名字不能为空')
            self.add.destroy()
        elif len(age) == 0:
            messagebox.showinfo('错误', '年龄不能为空')
            self.add.destroy()
        elif len(sex) == 0:
            messagebox.showinfo('错误', '性别不能为空')
            self.add.destroy()
        else:
            dd = lj.cursor()
            dd.execute(abb, [name, age, sex])
            lj.commit()
            dd.close()
            messagebox.showinfo('成功', '数据添加成功')
            self.add.destroy()


def main():
    ma = zhumain()
    ma.zhumain1()
    mainloop()
