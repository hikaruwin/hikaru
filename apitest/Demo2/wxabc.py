# coding: utf-8


# import wx

# class MainWindow(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(200, 100))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
#         self.Show(True)
#
# app = wx.App(False)
# frame = MainWindow(None, 'Small editor')
# app.MainLoop()

# class MyFrame(wx.Frame):
#     def __init__(self, parent, title):
#         wx.Frame.__init__(self, parent, title=title, size=(300,100))
#         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)

# class Frame(wx.Frame):
#
#     def __init__(self, image, parent=None, id=-1, pos=wx.DefaultPosition, title='Hello, wxPython!'):
#         temp = image.ConvertToBitmap()
#         size = temp.GetWidth(), temp.GetHeight()
#         wx.Frame.__init__(self, parent, id ,title, pos, size)
#         self.bmp = wx.StaticBitmap(parent=self, bitmap=temp)
#
# class App(wx.App):
#
#     def OnInit(self):
#         image = wx.Image('wxPython.jpg', wx.BITMAP_TYPE_JPEG)
#         self.frame = Frame(image)
#         self.frame.Show()
#         self.SetTopWindow(self.frame)
#         return True
#
# def main():
#     app = App()
#     app.MainLoop()
#
# if __name__ == '__main__':
#     main()

import wx
import sys

# class Frame(wx.Frame):
#
#     def __init__(self, parent, id, title):
#         print "Frame __init__"
#         wx.Frame.__init__(self, parent, id, title)
#
# class App(wx.App):
#
#     def __init__(self, redirect=True, filename=None):
#         print "App __init__"
#         wx.App.__init__(self, redirect, filename)
#
#     def OnInit(self):
#         print "OnInit"    #输出到stdout
#         self.frame = Frame(parent=None, id=-1, title='Startup')  #创建框架
#         self.frame.Show()
#         self.SetTopWindow(self.frame)
#         print    sys.stderr, "A pretend error message"    #输出到stderr
#         return True
#
#     def OnExit(self):
#         print "OnExit"
#
# if __name__ == '__main__':
#     app = App(redirect=True) #1 文本重定向从这开始
#     print "before MainLoop"
#     app.MainLoop()  #2 进入主事件循环
#     print "after MainLoop"

# class InsertFrame(wx.Frame):
#
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Frame With Button', size=(300, 100))
#         panel = wx.Panel(self)  # 创建画板
#         button = wx.Button(panel, label='close', pos=(125, 10), size=(50, 50))  # 按钮添加到画板
#         self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
#         self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
#
#     def OnCloseMe(self, event):
#         self.Close(True)
#
#     def OnCloseWindow(self, event):
#         self.Destroy()
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = InsertFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

import wx.py.images as images

# class ToolbarFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Toolbars',
#                 size=(300, 200))
#         panel = wx.Panel(self)
#         panel.SetBackgroundColour('White')
#         statusBar = self.CreateStatusBar() #1 创建状态栏
#         toolbar = self.CreateToolBar()     #2 创建工具栏
#         toolbar.AddSimpleTool(wx.NewId(), images.getPyBitmap(),
#                 "New", "Long help for 'New'") #3 给工具栏增加一个工具
#         toolbar.Realize() #4 准备显示工具栏
#         menuBar = wx.MenuBar() # 创建菜单栏
# # 创建两个菜单
#         menu1 = wx.Menu()
#         menuBar.Append(menu1, " ")
#         menu2 = wx.Menu()
# #6 创建菜单的项目
#         menu2.Append(wx.NewId(), " ", "Copy in status bar")
#         menu2.Append(wx.NewId(), "C ", "")
#         menu2.Append(wx.NewId(), "Paste", "")
#         menu2.AppendSeparator()
#         menu2.Append(wx.NewId(), " ", "Display Options")
#         menuBar.Append(menu2, " ") # 在菜单栏上附上菜单
#         self.SetMenuBar(menuBar)  # 在框架上附上菜单栏
#
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = ToolbarFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

# app = wx.App(False)
# dlg = wx.SingleChoiceDialog(None,
#         'What version of Python are you using?',
#         'Single Choice',
#         ['1.5.2', '2.0', '2.1.3', '2.2', '2.3.1'])
# if dlg.ShowModal() == wx.ID_OK:
#     response = dlg.GetStringSelection()
# # dlg.Destroy()
# app.MainLoop()

# class MenuEventFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Menus',
#              size=(300, 200))
#         menuBar = wx.MenuBar()
#         menu1 = wx.Menu()
#         menuItem = menu1.Append(-1, u"关闭")
#         menuBar.Append(menu1, u"文件")
#         self.SetMenuBar(menuBar)
#         self.Bind(wx.EVT_MENU, self.OnCloseMe, menuItem)
#
#     def OnCloseMe(self, event):
#         self.Close(True)
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = MenuEventFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

# class MouseEventFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Frame With Button',
#                           size=(300, 100))
#         self.panel = wx.Panel(self)
#         self.button = wx.Button(self.panel,
#                                 label="Not Over", pos=(100, 15))
#         self.Bind(wx.EVT_BUTTON, self.OnButtonClick,
#                   self.button)  # 1 绑定按钮事件
#         self.button.Bind(wx.EVT_ENTER_WINDOW,
#                          self.OnEnterWindow)  # 2 绑定鼠标位于其上事件
#         self.button.Bind(wx.EVT_LEAVE_WINDOW,
#                          self.OnLeaveWindow)  # 3 绑定鼠标离开事件
#
#     def OnButtonClick(self, event):
#         self.panel.SetBackgroundColour('Green')
#         self.panel.Refresh()
#
#     def OnEnterWindow(self, event):
#         self.button.SetLabel("Over Me!")
#         event.Skip()
#
#     def OnLeaveWindow(self, event):
#         self.button.SetLabel("Not Over")
#         event.Skip()
#
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = MouseEventFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

# class DoubleEventFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Frame With Button',
#                           size=(300, 100))
#         self.panel = wx.Panel(self, -1)
#         self.button = wx.Button(self.panel, -1, "Click Me", pos=(100, 15))
#         self.Bind(wx.EVT_BUTTON, self.OnButtonClick,
#                   self.button)  # 1 绑定按钮敲击事件
#         self.button.Bind(wx.EVT_LEFT_DOWN, self.OnMouseDown)  # 2 绑定鼠标左键按下事件
#
#     def OnButtonClick(self, event):
#         self.panel.SetBackgroundColour('Green')
#         self.panel.Refresh()
#
#     def OnMouseDown(self, event):
#         self.button.SetLabel("Again!")
#         event.Skip()  # 3 确保继续处理
#
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = DoubleEventFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

# class TwoButtonEvent(wx.PyCommandEvent):  # 1 定义事件
#     def __init__(self, evtType, id):
#         wx.PyCommandEvent.__init__(self, evtType, id)
#         self.clickCount = 0
#
#     def GetClickCount(self):
#         return self.clickCount
#
#     def SetClickCount(self, count):
#         self.clickCount = count
#
#
# myEVT_TWO_BUTTON = wx.NewEventType()  # 2 创建一个事件类型
# EVT_TWO_BUTTON = wx.PyEventBinder(myEVT_TWO_BUTTON, 1)  # 3 创建一个绑定器对象
#
#
# class TwoButtonPanel(wx.Panel):
#     def __init__(self, parent, id=-1, leftText="Left",
#                  rightText="Right"):
#         wx.Panel.__init__(self, parent, id)
#         self.leftButton = wx.Button(self, label=leftText)
#         self.rightButton = wx.Button(self, label=rightText,
#                                      pos=(100, 0))
#         self.leftClick = False
#         self.rightClick = False
#         self.clickCount = 0
#         # 4 下面两行绑定更低级的事件
#         self.leftButton.Bind(wx.EVT_LEFT_DOWN, self.OnLeftClick)
#         self.rightButton.Bind(wx.EVT_LEFT_DOWN, self.OnRightClick)
#
#     def OnLeftClick(self, event):
#         self.leftClick = True
#         self.OnClick()
#         event.Skip()  # 5 继续处理
#
#     def OnRightClick(self, event):
#         self.rightClick = True
#         self.OnClick()
#         event.Skip()  # 6 继续处理
#
#     def OnClick(self):
#         self.clickCount += 1
#         if self.leftClick and self.rightClick:
#             self.leftClick = False
#             self.rightClick = False
#             evt = TwoButtonEvent(myEVT_TWO_BUTTON, self.GetId())  # 7 创建自定义事件
#             evt.SetClickCount(self.clickCount)  # 添加数据到事件
#             self.GetEventHandler().ProcessEvent(evt)  # 8 处理事件
#
#
# class CustomEventFrame(wx.Frame):
#     def __init__(self, parent, id):
#         wx.Frame.__init__(self, parent, id, 'Click Count: 0',
#                           size=(300, 100))
#         panel = TwoButtonPanel(self)
#         self.Bind(EVT_TWO_BUTTON, self.OnTwoClick, panel)  # 9 绑定自定义事件
#
#     def OnTwoClick(self, event):  # 10 定义一个事件处理器函数
#         self.SetTitle("Click Count: %s" % event.GetClickCount())
#
#
# if __name__ == '__main__':
#     app = wx.PySimpleApp()
#     frame = CustomEventFrame(parent=None, id=-1)
#     frame.Show()
#     app.MainLoop()

class RefactorExample(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Refactor Example',size=(340, 200))
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour("White")
        prevButton = wx.Button(panel, -1, "   PREV", pos=(80, 0))
        self.Bind(wx.EVT_BUTTON, self.OnPrev, prevButton)
        nextButton = wx.Button(panel, -1, "NEXT   ", pos=(160, 0))
        self.Bind(wx.EVT_BUTTON, self.OnNext, nextButton)
        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        openMenuItem = menu1.Append(-1, " ", "Copy in status bar")
        self.Bind(wx.EVT_MENU, self.OnOpen, openMenuItem)
        quitMenuItem = menu1.Append(-1, " ", "Quit")
        self.Bind(wx.EVT_MENU, self.OnCloseWindow, quitMenuItem)
        menuBar.Append(menu1, " ")
        menu2 = wx.Menu()
        copyItem = menu2.Append(-1, " ", "Copy")
        self.Bind(wx.EVT_MENU, self.OnCopy, copyItem)
        cutItem = menu2.Append(-1, "C ", "Cut")
        self.Bind(wx.EVT_MENU, self.OnCut, cutItem)
        pasteItem = menu2.Append(-1, "Paste", "Paste")
        self.Bind(wx.EVT_MENU, self.OnPaste, pasteItem)
        menuBar.Append(menu2, " ")
        self.SetMenuBar(menuBar)

        static = wx.StaticText(panel, wx.NewId(), "First Name",
                pos=(10, 50))
        static.SetBackgroundColour("White")
        text = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 50))

        static2 = wx.StaticText(panel, wx.NewId(), "Last Name",
                pos=(10, 80))
        static2.SetBackgroundColour("White")
        text2 = wx.TextCtrl(panel, wx.NewId(), "", size=(100, -1),
                pos=(80, 80))

        firstButton = wx.Button(panel, -1, "FIRST")
        self.Bind(wx.EVT_BUTTON, self.OnFirst, firstButton)

        menu2.AppendSeparator()
        optItem = menu2.Append(-1, " ", "Display Options")
        self.Bind(wx.EVT_MENU, self.OnOptions, optItem)

        lastButton = wx.Button(panel, -1, "LAST", pos=(240, 0))
        self.Bind(wx.EVT_BUTTON, self.OnLast, lastButton)


    # Just grouping the empty event handlers together
    def OnPrev(self, event): pass
    def OnNext(self, event): pass
    def OnLast(self, event): pass
    def OnFirst(self, event): pass
    def OnOpen(self, event): pass
    def OnCopy(self, event): pass
    def OnCut(self, event): pass
    def OnPaste(self, event): pass
    def OnOptions(self, event): pass

    def OnCloseWindow(self, event):
        self.Destroy()

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = RefactorExample(parent=None, id=-1)
    frame.Show()
    app.MainLoop()