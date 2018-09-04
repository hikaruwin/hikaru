# coding:utf-8

from Tkinter import *

class WidgetsDemo:
    def __init__(self):
        window = Tk()
        window.title(u'忘却难免留个疤')
        # 添加一个多选按钮和单选按钮到frame1
        frame1 = Frame(window)
        frame1.pack()  # 看下面的解释（包管理器）
        self.v1 = IntVar()
        cbtBold = Checkbutton(frame1, text = u"粗体", variable = self.v1, command = self.processCheckbutton)
        self.v2 = IntVar()
        rbRed = Radiobutton(frame1, text = u"红色", bg = u"red", variable = self.v2, value = 1, command = self.processRaidobutton)
        rbYellow = Radiobutton(frame1, text=u"黄色", bg=u"yellow", variable=self.v2, value=2, command=self.processRaidobutton)
        cbtBold.grid(row = 1, column = 1)  # 将cbtBold排列在frame1的网格第一行第一列（网格管理器也会在下面有解释）
        rbRed.grid(row=1, column=2)
        rbYellow.grid(row=1, column=3)
        # 添加一个label、entry、button和message到frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text = u"请输入名字")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = u"获取名字", command = self.processButton)
        message = Message(frame2, text = u"组建demo")
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)
        text = Text(window)
        text.pack()
        text.insert(END, u"Tip 最好的学习方式是活的比别人更长")  # END表示插入到当前文本最后
        text.insert(END, u"活上一万年就什么")
        text.insert(END, u"都能学会")
        window.mainloop()

    def processCheckbutton(self):
        print(u"复选框按钮是" + (u"被选中" if self.v1.get() == 1 else u"未选中"))
    def processRaidobutton(self):
        print(u"红色是" + (u"被选中" if self.v2.get() == 1 else u"未选中"))
    def processButton(self):
        print(u"你的名字是：" + self.name.get())
WidgetsDemo()
