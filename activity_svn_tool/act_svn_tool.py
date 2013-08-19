#!#!/usr/bin/python
#-*- coding:utf-8 -*-

import os, sys
try:
    from tkinter import *
except ImportError:  #Python 2.x
    PythonVersion = 2
    from Tkinter import *
    from tkFont import Font
    from ttk import *
    #Usage:showinfo/warning/error,askquestion/okcancel/yesno/retrycancel
    from tkMessageBox import *
    #Usage:f=tkFileDialog.askopenfilename(initialdir='E:/Python')
    #import tkFileDialog
    #import tkSimpleDialog
else:  #Python 3.x
    PythonVersion = 3
    from tkinter.font import Font
    from tkinter.ttk import *
    from tkinter.messagebox import *
    #import tkinter.filedialog as tkFileDialog
    #import tkinter.simpledialog as tkSimpleDialog    #askstring()

class Application_ui(Frame):
    #这个类仅实现界面生成功能，具体事件处理代码在子类Application中。
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.title('Form1')
        self.master.geometry('753x361')
        self.createWidgets()

    def createWidgets(self):
        self.top = self.winfo_toplevel()

        self.style = Style()

        self.upload = Button(self.top, text=u'上传', command=self.upload_Cmd)
        self.upload.place(relx=0.181, rely=0.82, relwidth=0.108, relheight=0.136)

        self.Text2Var = StringVar(value='Text2')
        self.Text2 = Entry(self.top, text='Text2', textvariable=self.Text2Var)
        self.Text2.place(relx=0.032, rely=0.443, relwidth=0.416, relheight=0.069)

        self.Text1Var = StringVar(value='Text1')
        self.Text1 = Entry(self.top, text='Text1', textvariable=self.Text1Var)
        self.Text1.place(relx=0.032, rely=0.177, relwidth=0.416, relheight=0.069)

        self.confirm = Button(self.top, text=u'确认打包', command=self.confirm_Cmd)
        self.confirm.place(relx=0.032, rely=0.82, relwidth=0.108, relheight=0.136)

        self.quit = Button(self.top, text=u'退出', command=self.top.destroy)
        self.quit.place(relx=0.329, rely=0.82, relwidth=0.108, relheight=0.136)

        self.List1Var = StringVar(value='List1')
        self.List1 = Listbox(self.top, listvariable=self.List1Var)
        self.List1.place(relx=0.489, rely=0.044, relwidth=0.49, relheight=0.936)

        self.style.configure('Label2.TLabel',anchor='w')
        self.Label2 = Label(self.top, text=u'包文件位置', style='Label2.TLabel')
        self.Label2.place(relx=0.032, rely=0.332, relwidth=0.193, relheight=0.069)

        self.style.configure('Label1.TLabel',anchor='w')
        self.Label1 = Label(self.top, text=u'列表文件位置', style='Label1.TLabel')
        self.Label1.place(relx=0.032, rely=0.066, relwidth=0.182, relheight=0.069)


class Application(Application_ui):
    #这个类实现具体的事件处理回调函数。界面生成代码在Application_ui中。
    def __init__(self, master=None):
        Application_ui.__init__(self, master)

    def upload_Cmd(self, event=None):
        #TODO, Please finish the function here!
        pass

    def confirm_Cmd(self, event=None):
        #TODO, Please finish the function here!
        self.Text1.setvar('text', 'fsadf')
        pass

if __name__ == "__main__":
    top = Tk()
    Application(top).mainloop()
    try: top.destroy()
    except: pass
