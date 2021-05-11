#!/user/bin/env python3
# -*- coding = utf-8 -*-
_author_ = 'tq'
from tkinter import *

import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'dt78'
}


class shuchumain():
    def pri_1(self):
        self.t.delete(1.0, 'end')
        name = self.entry.get()
        pri1 = self.lj.cursor()
        pri1.execute(self.b, name)
        i = pri1.fetchall()
        if len(i) > 0:
            for io in i:
                self.t.insert('insert', '学号：%d ，名字：%s ，年龄：%d，性别：%s\n' % (io[0], io[2], io[1], io[3]))
            pri1.close()
        else:
            self.t.insert('insert', '没有该学生的信息！！！\n')
            pri1.close()

    def pri_2(self):
        pri1 = self.lj.cursor()
        pri1.execute(self.a)
        self.t.delete(1.0, 'end')
        for io in pri1.fetchall():
            self.t.insert('insert', '学号：%d ，名字：%s ，年龄：%d，性别：%s\n' % (io[0], io[2], io[1], io[3]))
        pri1.close()

    def __init__(self):
        self.a = '''
        select * from student
                '''
        self.b = '''
        select * from student where stu_name=%s
                '''
        self.lj = pymysql.connect(**config)
        self.pri = Tk()
        self.pri.title('输出学生信息')
        self.pri.geometry('500x350')
        self.label = Label(self.pri, text='请选择需要输出的学生的姓名')
        self.entry = Entry(self.pri)
        self.button = Button(self.pri, text='确认', command=self.pri_1)
        self.button1 = Button(self.pri, text='输出所有的学生信息', command=self.pri_2)
        self.t = Text(self.pri)

    def shuchumain1(self):
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.button1.pack()
        self.t.pack()
        self.pri.mainloop()


def main():
    ma = shuchumain()
    ma.shuchumain1()
    #mainloop()
