# coding: utf-8

from Tkinter import *
from case import crmAdd
from case.basetestcase import *
from Demo2.crmRegister import crmre

class WidgetsDemo:
    # userid = '2'
    # teacherid = '3'
    # starttime = 'r'
    # global elist
    # elist = []
    def __init__(self):
        global entrySphone
        global entryTphone
        global entryTime
        global entryCid
        global entryrequest
        global var
        global label5
        global entryUser

        root = Tk()
        root.title('正式环境一键注册v1.0.1')
        # root.geometry('640x480')
        # root.resizable(width=True, height=False)
        # showinfo(title=u'注意事项', message=u'只能在测试环境下使用该工具')
        frame1 = Frame(root)
        frame1.pack()
        label = Label(frame1, text=u"请输入注册账号的手机号")
        # self.sphone = StringVar()
        # entrySphone = Entry(frame1, textvariable=self.sphone)
        entrySphone = Entry(frame1)
        # btGetSphone = Button(frame1, text=u"获取学生手机号")
        # global userid
        # userid = self.sphone.get()
        label.grid(row=1, column=1)
        entrySphone.grid(row=1, column=2)
        # elist.append(entrySphone)
        # btGetSphone.grid(row=1, column=3)
        label1 = Label(frame1, text=u'请输入注册账号的昵称')
        # tphone = StringVar()
        # entryTphone = Entry(frame1, textvariable=self.tphone)
        entryUser = Entry(frame1)
        # btGetTphone = Button(frame1, text=u'获取老师手机号')
        # global teacherid
        # teacherid = self.tphone.get()
        label1.grid(row=2, column=1)
        entryUser.grid(row=2, column=2)
        # elist.append(entryTphone)
        # btGetTphone.grid(row=2, column=3)
        # label2 = Label(frame1, text=u'请输入注册账号的密码，默认123456a')
        # self.time = StringVar()
        # entryTime = Entry(frame1, textvariable=self.time)
        # entryPaw = Entry(frame1)
        # btGetTime = Button(frame1, text=u'获取上课时间')
        # global starttime
        # starttime = self.time.get()
        # label2.grid(row=3, column=1)
        # entryPaw.grid(row=3, column=2)
        # elist.append(entryTime)
        # print elist
        # btGetTime.grid(row=3, column=3)
        btreg = Button(frame1, text=u'注册', command=self.btReg)
        btreg.grid(row=4, column=2)
        global m
        m = Label(frame1, text='')
        m.grid(row=5, column=1, columnspan=2)
        # label3 = Label(frame1, text=u'请输入课程id')
        # entryCid = Entry(frame1)
        # btDeleteClass = Button(frame1, text=u'取消课', command=self.deleteClass)
        # label3.grid(row=6, column=1)
        # entryCid.grid(row=6, column=2)
        # btDeleteClass.grid(row=7, column=2)
        # global m2
        # m2 = Label(frame1, text='')
        # m2.grid(row=8, column=1, columnspan=2)
        # label4 = Label(frame1, text=u'手机号请求验证码')
        # entryrequest = Entry(frame1)
        # btRequest = Button(frame1, text=u'请求', command=self.btRequest)
        # var = IntVar()
        # r1 = Radiobutton(frame1, text=u'忘记密码', variable=var, value=1)
        # r2 = Radiobutton(frame1, text=u'注册', variable=var, value=2)
        # r3 = Radiobutton(frame1, text=u'验证码登录', variable=var, value=3)
        # label5 = Label(frame1, text='')
        # label4.grid(row=9, column=1)
        # entryrequest.grid(row=9, column=2)
        # r1.grid(row=10, column=1)
        # r2.grid(row=10, column=2)
        # r3.grid(row=10, column=3)
        # btRequest.grid(row=11, column=2)
        # label5.grid(row=12, column=1, columnspan=2)



        root.mainloop()

    def btReg(self):
        reqPhone = entrySphone.get()
        reqUser = entryUser.get()
        # rtype = var.get()
        r = crmre(reqPhone, reqUser)
        mess = r[u'message']
        # code = str((r['data'])['code'])
        if mess == u'成功':
            # code = str((r['data'])['code'])
            m['text'] = u'注册成功'
        else:
            m['text'] = u'操作失败：'+mess



    # def deleteClass(self):
    #     classid1 = entryCid.get()
    #     d = crmDelete(classid=classid1)
    #     error = d[u'error']
    #     if error == '':
    #     # print error
    #         m2['text'] = u'操作成功'
    #     else:
    #         m2['text'] = u'操作失败：'+error
    #
    #
    # def addClass(self):
    #     userphone = entrySphone.get()
    #     teacherphone = entryTphone.get()
    #     starttime = entryTime.get()
    #     # key = ('userid', 'teacherid', 'starttime')
    #     # dict1 = dict(zip(key, elist))
    #     # print userid
    #     # u = req('https://xiaohei-api.dev.pnlyy.com/v4/login/login', '', '', '2.1.0', '0', '192.168.56.1', 'sdsdasd',
    #     #         '1', username=userphone, pwd='123456a', type='0', areaCode='+86')
    #     # print r
    #     # self.assertEqual(u'成功', r[u'message'])
    #     # print r[u'data']
    #     # print type(r[u'data'])
    #     # print (r[u'data'])[u'uid']
    #     # print type((r[u'data'])[u'uid'])
    #     # global uid
    #     uid = selectMySql_user(user=userphone)
    #     # uid = (u['data'])['uid']
    #     print uid
    #     # print type(uid)
    #     # global accessUser
    #     # accessUser = (r['data'])['accessToken']
    #     # print accessUser
    #     # t = req('https://xiaohei-api.dev.pnlyy.com/v4/login/login', '', '', '2.1.0', '1', '192.168.56.1', 'sdsdasd',
    #     #         '2', username=teacherphone, pwd='123456', type='2', areaCode='+86')
    #     # print r
    #     # print type(r)
    #     # self.assertEqual(u'成功', r[u'message'])
    #     # global uid
    #     teacherid = selectMySql_teacher(teacher=teacherphone)
    #     print teacherid
    #     # teacherid = (t['data'])['uid']
    #     # print
    #     # global accessUser
    #     # accessUser = (r['data'])['accessToken']
    #     # print accessUser
    #
    #
    #     t = crmAdd.crm(userid=uid, teacherid=teacherid, starttime=starttime)
    #     print t
    #     error = t[u'error']
    #     if error == '':
    #     # print error
    #         cid = str(t['data']['class_id'])
    #         m['text'] = u'操作成功，课程id:'+cid
    #     else:
    #         m['text'] = u'操作失败：'+error





    # def getStudentButton(self):
    #     userid = self.sphone.get()
    #     print(u"学生的手机号是：" + self.sphone.get())
    #     return userid
    #
    # def getTeacherButton(self):
    #     teacherid = self.tphone.get()
    #     print(u"老师的手机号是：" + self.tphone.get())
    #     return teacherid
    #
    # def getTimeButton(self):
    #     starttime = self.time.get()
    #     print(u"获取的时间是：" + self.time.get())
    #     return starttime


# t = Text(root)
# t.insert('1.0', 'text1\n')
# t.insert(END, 'text2\n')
# t.insert('1.0', 'text3\n')
# t.pack()
if __name__ == '__main__':
    WidgetsDemo()
# crm(userid, teacherid, starttime)