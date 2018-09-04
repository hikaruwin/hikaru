# coding: utf-8

import easygui as g
import sys

reload(sys)
sys.setdefaultencoding( "utf-8" )

while 1:
    g.msgbox(u'嗨，欢迎进入第一个界面小游戏^_^')
    msg = u'请问你希望在鱼C工作室学生到什么知识呢？'
    title = u'小游戏互动'
    choices = [u'谈恋爱', u'编程', u'OOXX', u'琴棋书画']
    choice = g.choicebox(msg, title, choices)
    g.msgbox(u'你的选择是：'+str(choice), u'结果')
    msg1 = u'你希望重新开始小游戏吗？'
    title1 = u'请选择'
    if g.ccbox(msg1, title1):
        pass
    else:
        sys.exit(0)