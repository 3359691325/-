#!/user/bin/env python3
# -*- coding = utf-8 -*-
_author_ = 'tq'
from tkinter import *
from tkinter import messagebox
import shanmain2
import pymysql

config = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'dt78'
}
class shanmain():
    def delete(self):
        san = '''
        select * from student where stu_name=%s       
                '''
        san1 = '''
        delete from student where stu_name=%s
                '''
        lj = pymysql.connect(**config)
        an = lj.cursor()
        name = self.entry1.get()
        # 判断是否输入了数值 没有的话旧退出
        if len(name) == 0:
            messagebox.showinfo('请不要留空姓名', '')
        else:
            i = an.execute(san, name)
            if i > 1:
                c = an.fetchall()
                self.shan.destroy()
                shanmain2.main(c)
            elif i < 1:
                messagebox.showinfo('错误', '找不到该学生信息，请检查是否输入错误')
                an.close()
                self.shan.destroy()
            elif i == 1:
                an.execute(san1, name)
                lj.commit()
                an.close()
                messagebox.showinfo('成功', '删除成功')
                self.shan.destroy()



    def __init__(self):
        #self.an = lj.cursor()
        self.shan = Tk()
        self.shan.title('删除学生信息')
        self.shan.geometry('500x350')
        self.table1 = Label(self.shan, text='请输入要删除的学生姓名')
        self.entry1 = Entry(self.shan)
        self.button1 = Button(self.shan, text='确认', command=self.delete)
    def shanmain1(self):
        self.table1.pack()
        self.entry1.pack()
        self.button1.pack()

def main():
    ma = shanmain()
    ma.shanmain1()
    mainloop()