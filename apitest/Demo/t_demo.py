# coding: utf-8

from Tkinter import *

def xinlabel(event):
    global xin
    s = Label(xin, text=u'我爱python')
    s.pack()

xin = Tk()
# b1 = Button(xin, text=u'英格', command=xinlabel)
# b1.pack()
t = Label(xin, text='模拟按钮')
t.bind('<Button-3>', xinlabel)
t.pack()

xin.mainloop()