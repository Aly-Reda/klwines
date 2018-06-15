#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/06/14 
# @Author  : Aly Reda
# @Site    : 
# @File    : GUI.py

#user               = 'samir.ahmed.abdelazem@gmail.com'
#password           ='123456789asd!@#'
#sendto             = 'samir.ahmed.abdelazem@gmail.com'






from web.get import scrape as code
from web.data import compare as date

from web.Gmail import get 
import re

from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.title("Klwines Scraping")
win.iconbitmap(r'klwines1.ico')

global Statusrow
global Statuscolumnspan
global ButtonCol
Statusrow =10
Statuscolumnspan =12
ButtonCol=10







#Menu Bar
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Logs")
filemenu.add_command(label="Automatic")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_separator()
filemenu2.add_command(label="About Klwines", command=win.quit)
menubar.add_cascade(label="Options", menu=filemenu)
menubar.add_cascade(label="Help", menu=filemenu2)
win.config(menu=menubar)



row = 0
# Frame 1


#label Choose Category
ttk.Label(win,text = "Choose Category:").grid(column=0,row=row)

row+=1

#Combobox
number = tk.StringVar()
numberChosen = ttk.Combobox(win,width=12,textvariable=number,state='readonly')
numberChosen['values']=('Beer','Distilled Spirits','Other','Sake','Soda','Wine - Dessert','Wine - Red','Wine - Rose','Wine - Sparkling','Wine - White')
numberChosen.grid(column = 0, row = row , columnspan=8, sticky="we")
numberChosen.current(1)


#Button Scrape
def ClickAction():
    website_status= code.Check_Connection()
    status = Label(win, text=website_status,bd=1 , relief =SUNKEN , anchor=W )
    status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")


    if website_status == 'Website Working':
        
        wine_list={'Beer':7 ,'Distilled Spirits':10 ,'Other':0 ,'Sake':23 ,'Soda':15 ,'Wine - Dessert':5 ,'Wine - Red':1 ,'Wine - Rose':3 ,'Wine - Sparkling':4 ,'Wine - White':2}
        idf=wine_list[str(number.get())]
        sc=(code.data(idf))
        status = Label(win, text="Scraping "+sc+"-"+ number.get()+" Done" ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

        if chVarUn.get() == 1:
            code.json()
            

action = ttk.Button(win,text = "Scrape" ,command=ClickAction).grid(column = ButtonCol, row = row)




# Frame 2
row+=1

#label Gmail
aLabel = ttk.Label(win , text = 'Gmail:')
aLabel.grid(column = 0, row = row , columnspan=1, sticky="we")

#label Password
aLabel2 = ttk.Label(win , text = 'Password:')
aLabel2.grid(column = 1, row = row , columnspan=1, sticky="we")

row+=1
#FieldText Gmail
#def OnWriteEmail():
    
 #   if not re.match(r"^[a-z0-9](\.?[a-z0-9]){5,}@g(oogle)?mail\.com$", name.get()):
  #      status = Label(win, text='Please Enter a Correct Gmail' ,bd=1 , relief =SUNKEN , anchor=W )
   #     status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
    #else:
     #   status = Label(win, text='match' ,bd=1 , relief =SUNKEN , anchor=W )
      #  status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
#validatecommand= OnWriteEmail
#global name


name = tk.StringVar()
nameEntered = ttk.Entry(win,width=12,textvariable=name )
nameEntered.grid(column=0,row = row , columnspan=1, sticky="we")
nameEntered.insert(0, '@gmail.com')
#nameEntered.focus()



#FieldText Password
password = tk.StringVar()
passwordEntered = ttk.Entry(win, show="*",width=12,textvariable=password)
passwordEntered.grid(column=1,row = row , columnspan=1, sticky="we")
passwordEntered.focus()

#CheckBox Keep
def inCheck1():
    keep=Keep1.get()
    if keep == 1:
        nameEntered = ttk.Entry(win,width=12,textvariable=name , state = 'disabled' )
        nameEntered.grid(column=0,row = 3 , columnspan=1, sticky="we")
        passwordEntered = ttk.Entry(win, show="*",width=12,textvariable=password , state = 'disabled')
        passwordEntered.grid(column=1,row = 3 , columnspan=1, sticky="we")
        
    elif keep == 0:
        nameEntered = ttk.Entry(win,width=12,textvariable=name )
        nameEntered.grid(column=0,row = 3 , columnspan=1, sticky="we")
        passwordEntered = ttk.Entry(win, show="*",width=12,textvariable=password)
        passwordEntered.grid(column=1,row = 3 , columnspan=1, sticky="we")



Keep1 = tk.IntVar()
Keep1check1 = tk.Checkbutton(win, text = "Keep" , variable = Keep1 ,command= inCheck1)
Keep1check1.grid(column = 3, row = row, sticky = tk.W)


#Button Check
def ClickAction2():
    Gmail_Status=get.login_check(name.get(),password.get())
    print(Gmail_Status)
    if Gmail_Status == 'Login Successful':
        status = Label(win, text=Gmail_Status ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

            
    elif Gmail_Status == 'Login Failed':
        status = Label(win, text=Gmail_Status ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
        x=messagebox.showerror("Error", 'Please Check Name,Password & Enabling Third Party at Gmail')
        if x=='ok':
            status = Label(win, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")



action1 = ttk.Button(win,text = "Connect" ,command= ClickAction2 ).grid(column = ButtonCol, row = row)







# Frame 3
row+=1

#label Send To
aLabel = ttk.Label(win , text = 'Send To:')
aLabel.grid(column = 0, row = row , columnspan=1, sticky="we")


row+=1
#FieldText Send To
#global SendEmail
SendEmail = tk.StringVar()
SendEmailEntered = ttk.Entry(win,width=12,textvariable=SendEmail)
SendEmailEntered.grid(column=0,row = row , columnspan=2, sticky="we")
SendEmailEntered.focus()

#CheckBox Keep

def inCheck2():
    keep=Keep2.get()
    if keep == 1:
        SendEmailEntered = ttk.Entry(win,width=12,textvariable=SendEmail , state = 'disabled' )
        SendEmailEntered.grid(column=0,row = 5 , columnspan=2, sticky="we")
        
    elif keep == 0:
        SendEmailEntered = ttk.Entry(win,width=12,textvariable=SendEmail )
        SendEmailEntered.grid(column=0,row = 5 , columnspan=2, sticky="we")



Keep2 = tk.IntVar()
Keep2check1 = tk.Checkbutton(win, text = "Keep" , variable = Keep2 , command= inCheck2)
Keep2check1.grid(column = 3, row = row, sticky = tk.W)

#Button Check


def ClickAction3():
    #user               = 'samir.ahmed.abdelazem@gmail.com'
    #password           ='123456789asd!@#'
    #sendto             = 'samir.ahmed.abdelazem@gmail.com'
    user               =name.get()
    password1           = password.get()
    sendto             = SendEmail.get()
    
##    try:    
    #ahmed.email_send(user,password,sendto)
    if chVarUn.get() == 0:
        get.email_send(user,password1,sendto)
        status = Label(win, text="Email Send with Excel.",bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

    elif chVarUn.get() == 1:
        get.email_send_two_attachments(user,password1,sendto)
        status = Label(win, text="Email Send with Excel & json.",bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
##    except:
##        status = Label(win, text="Enter Email & Password.",bd=1 , relief =SUNKEN , anchor=W )
##        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")


action3 = ttk.Button(win,text = "SEND" ,command=ClickAction3).grid(column = ButtonCol, row = row)





row+=1
# Frame 4
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text = "Excel" , variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = row, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text = 'Json', variable = chVarUn)
check2.deselect()
check2.grid(column =  1, row = row, sticky=tk.N)














#Frame Status
status = Label(win, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")


#Exit
def protocolhandler():
    if messagebox.askokcancel("Exit", "Wanna leave?"):
        win.destroy()

win.protocol("WM_DELETE_WINDOW", protocolhandler)
win.mainloop()






##
##try
##group = LabelFrame(win, text="Group", bd=1,padx=5, pady=5)
##group.grid(row=9, column=0, columnspan=3, sticky="we")
##









##
##
##wine_list={'Beer':7 ,
## 'Distilled Spirits':10 ,
## 'Other':0 ,
## 'Sake':23 ,
## 'Soda':15 ,
## 'Wine - Dessert':5 ,
## 'Wine - Red':1 ,
## 'Wine - Rose':3 ,
## 'Wine - Sparkling':4 ,
## 'Wine - White':2 }



    #action.configure(text="** I have been Scraped! **" + name.get() + number.get())
    #aLabel.configure(foreground='red')




#Disable the Button Widget
#action.configure(state='disabled')

#ttk.Label(win, text = '').grid(column=0,row=0)



    #elif website_status == 'Website Down':
     #   status1 = Label(win, text=website_status,bd=1 , relief =SUNKEN , anchor=W )
      #  status1.grid(row=5, column=0, columnspan=3, sticky="we")

    #elif website_status == 'No Internet Connection':
     #   status1 = Label(win, text=website_status,bd=1 , relief =SUNKEN , anchor=W )
      #  status1.grid(row=5, column=0, columnspan=3, sticky="we")
    #action.configure(text="** I have been Scraped! **" + name.get() + number.get())
    #aLabel.configure(foreground='red')






#time = tk.StringVar()
#timeEntered = ttk.Entry(win, width=10,textvariable=time)
#timeEntered.insert(0, 'time in sec')
#timeEntered.grid(column=1,row = 4)
#timeEntered.focus()

#The reson why it became so small is that we added a widget to our form. Without
#a widget ,tkinter uses a default size.


#import win32gui, win32con
#The_program_to_hide = win32gui.GetForegroundWindow()
#win32gui.ShowWindow(The_program_to_hide , win32con.SW_HIDE)
#from distutils.core import setup
#import py2exe
#setup (console = ['GUI.py'],
 #      options = { 'py2exe' : {'packages':['Tkinter']}})
#import web.compare.compare 
#import web.email.get 
#from web.get import idfilter as idf
#d=StatusBar(win)
#win.geometry('300x100')
#win.mainloop()

#ttk.Label(win,text="Hello World!").grid(column=0,row = 0)




#aLabel3 = ttk.Label(win , text = 'sec:')
#aLabel3.grid(column = 0, row = 4)


#chVarEn = tk.IntVar()
#check3 = tk.Checkbutton(win,text='Enabled',variable=chVarEn)
#check3.select()
#check3.grid(column = 2, row = 4 ,sticky = tk.W)
