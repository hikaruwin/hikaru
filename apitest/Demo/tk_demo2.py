# coding: utf-8

from Tkinter import *

class WidgetsDemo:
    def __init__(self):
        root = Tk()
        root.title('排课')
        root.geometry('400x400')
        root.resizable(width=True, height=False)
        frame1 = Frame(root)
        frame1.pack()
        label = Label(frame1, text=u"请输入学生手机号")
        self.sphone = StringVar()
        entrySphone = Entry(frame1, textvariable=self.sphone)
        btGetSphone = Button(frame1, text=u"获取学生手机号", command=self.getStudentButton)
        label.grid(row=1, column=1)
        entrySphone.grid(row=1, column=2)
        btGetSphone.grid(row=1, column=3)
        label1 = Label(frame1, text=u'请输入老师手机号')
        self.tphone = StringVar()
        entryTphone = Entry(frame1, textvariable=self.tphone)
        btGetTphone = Button(frame1, text=u'获取老师手机号', command=self.getTeacherButton)
        label1.grid(row=2, column=1)
        entryTphone.grid(row=2, column=2)
        btGetTphone.grid(row=2, column=3)
        label2 = Label(frame1, text=u'请输入排课时间,如2017-12-12 20:00')
        self.time = StringVar()
        entryTime = Entry(frame1, textvariable=self.time)
        btGetTime = Button(frame1, text=u'获取上课时间', command=self.getTimeButton)
        label2.grid(row=3, column=1)
        entryTime.grid(row=3, column=2)
        btGetTime.grid(row=3, column=3)


        root.mainloop()


    def getStudentButton(self):
        print(u"学生的手机号是：" + self.sphone.get())

    def getTeacherButton(self):
        print(u"老师的手机号是：" + self.tphone.get())

    def getTimeButton(self):
        print(u"老师的手机号是：" + self.time.get())
# t = Text(root)
# t.insert('1.0', 'text1\n')
# t.insert(END, 'text2\n')
# t.insert('1.0', 'text3\n')
# t.pack()
WidgetsDemo()

