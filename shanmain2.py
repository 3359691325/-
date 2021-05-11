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
class shanmain2():
    def id_1(self):
        san1 = '''
        delete from student where stu_id=%s
                                                '''
        id = self.entry.get()
        bb = self.lj.cursor()
        bb.execute(san1, id)
        self.lj.commit()
        bb.close()
        messagebox.showinfo('成功', '删除成功')
        self.cc.destroy()

    def __init__(self,c):
        self.c = c
        self.lj = pymysql.connect(**config)
        self.cc = Tk()
        self.cc.geometry('300x200')
        self.label = Label(self.cc, text='请输入id')
        self.entry = Entry(self.cc)
        self.button = Button(self.cc, text='确定', command=self.id_1)
        self.t = Text(self.cc)

    def shanmain12(self):
        self.label.pack()
        self.entry.pack()
        self.button.pack()
        self.t.pack()
        self.t.insert('insert', '搜索到多条数据 请选择id进行删除\n')
        for io in self.c:
            self.t.insert('insert', '学号：%d ，名字：%s ，年龄：%d，性别：%s\n' % (io[0], io[2], io[1], io[3]))

def main(c):
    ma = shanmain2(c)
    ma.shanmain12()
    mainloop()