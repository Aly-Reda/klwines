#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/06/14 
# @Author  : Aly Reda
# @Site    : 
# @File    : GUI.py
 

    #user               = 'samir.ahmed.abdelazem@gmail.com'
    #password           ='123456789asd!@#'
    #sendto             = 'samir.ahmed.abdelazem@gmail.com'

import pickle

from web.get import scrape as code
from web.Gmail import get  as sendData 
import re

from tkinter import *  
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

win = tk.Tk()
win.title("Klwines Scraping")
win.iconbitmap(r'klwines.ico')
#win.geometry('350x240')
win.resizable(False, False)

#center
# Gets the requested values of the height and widht.
#windowWidth = win.winfo_reqwidth()
#windowHeight = win.winfo_reqheight()
#print("Width",windowWidth,"Height",windowHeight)
# Gets both half the screen width/height and window width/height
#positionRight = int(win.winfo_screenwidth() - windowWidth)
#positionDown = int(win.winfo_screenheight() - windowHeight)
# Positions the window in the center of the page.
#win.geometry("+{}+{}".format(positionRight, positionDown))


file_store=[]  
try:
    with open('data.pickle', 'rb') as f:
        data = pickle.load(f)
    file_store=data
except:
    file_store=['0','0','','','']

print('file stored',file_store)


global Statusrow
global Statuscolumnspan
global ButtonCol
Statusrow =10
Statuscolumnspan =12
ButtonCol=10

wine_list={'Beer':7 ,'Distilled Spirits':10 ,'Other':0 ,'Sake':23 ,'Soda':15 ,'Wine - Dessert':5 ,'Wine - Red':1 ,'Wine - Rose':3 ,'Wine - Sparkling':4 ,'Wine - White':2}
import os



#tabs
tab_control = ttk.Notebook(win)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)

tab_control.add(tab1, text='    Manual    ')
tab_control.add(tab2, text='    Schedule    ')
tab_control.add(tab3, text='    Logs     ')
tab_control.add(tab4, text='   About Klwines ')


#lbl2 = Label(tab2, text= 'label2')
#lbl2.grid(column=0, row=0)

tab_control.pack(expand=1, fill='both', padx = 10, pady = 10)










#Menu Bar
menubar = Menu(win)
filemenu = Menu(menubar, tearoff=0)

def Schedulemenuclick():
    tab_control.select(tab2)
filemenu.add_command(label="Schedule" ,  command = Schedulemenuclick)


def logsmenuclick():
    tab_control.select(tab3)
    
filemenu.add_command(label="Logs" , command =logsmenuclick)


filemenu.add_separator()
filemenu.add_command(label="Exit", command=win.quit)
filemenu2 = Menu(menubar, tearoff=0)
filemenu2.add_separator()

def aboutmenuclick():
    tab_control.select(tab4)

filemenu2.add_command(label="About Klwines", command=aboutmenuclick)

menubar.add_cascade(label="Options", menu=filemenu)
menubar.add_cascade(label="Help", menu=filemenu2)
win.config(menu=menubar)






row = 0
# Frame 1


#label Choose Category
ttk.Label(tab1,text = "Choose Category:").grid(column=0,row=row)

row+=1

#Combobox
number = tk.StringVar()
numberChosen = ttk.Combobox(tab1,width=12,textvariable=number,state='readonly')
numberChosen['values']=('Beer','Distilled Spirits','Other','Sake','Soda','Wine - Dessert','Wine - Red','Wine - Rose','Wine - Sparkling','Wine - White')
numberChosen.grid(column = 0, row = row , columnspan=8, sticky="we")
numberChosen.current(1)

#Button Scrape
def ClickAction():
    scrape=code()
    internet_connection = scrape.internet() 
    website_status= scrape.Check_Connection()
    status = Label(tab1, text=website_status,bd=1 , relief =SUNKEN , anchor=W )
    status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
    if internet_connection == True:

        if website_status == 'Website Working':
            idf=wine_list[str(number.get())]
            #print(idf)
            scrape=code(idf)
            scrape.data()
            status = Label(tab1, text="Scraping "+str(idf)+"-"+ number.get()+" Done" ,bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            x=messagebox.showinfo(message= "Scraping "+str(idf)+"-"+ number.get()+" Done" )
            if x=='ok':
                status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            
            if chVarUn.get() == 1:
                scrape.json()
        else:
            status = Label(tab1, text="Please wait until the website back" ,bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            x=messagebox.showinfo(message= "Please wait until the website back" )
            if x=='ok':
                status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
    else:
        status = Label(tab1, text="Please check the internet connection" ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
        x=messagebox.showinfo(message= "Please check the internet connection" )
        if x=='ok':
            status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
 

action = ttk.Button(tab1,text = "Scrape" ,command=ClickAction).grid(column = ButtonCol, row = row)


# Frame 2
row+=1

#label Gmail
aLabel = ttk.Label(tab1 , text = 'Gmail:')
aLabel.grid(column = 0, row = row , columnspan=1, sticky="we")

#label Password
aLabel2 = ttk.Label(tab1 , text = 'Password:')
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
nameEntered = ttk.Entry(tab1,width=12,textvariable=name )
nameEntered.grid(column=0,row = row , columnspan=1, sticky="we")
if file_store !=[0,0,"","",""]:
    nameEntered.insert(0, file_store[2])
else:
    nameEntered.insert(0, '')



#nameEntered.focus()



#FieldText Password
password = tk.StringVar()
passwordEntered = ttk.Entry(tab1, show="*",width=12,textvariable=password)
passwordEntered.grid(column=1,row = row , columnspan=1, sticky="we")
if file_store !=[0,0," "," "," "]:
    passwordEntered.insert(0, file_store[3])
else:
    passwordEntered.insert(0, '')




#passwordEntered.focus()

#CheckBox Keep
Keep1 = tk.IntVar()
Keep1check1 = tk.Checkbutton(tab1, text = "Keep" , variable = Keep1)
Keep1check1.grid(column = 3, row = row, sticky = tk.W)
if file_store[0] == '1':
    Keep1check1.select()


#Button Check
def ClickAction2():
    send=sendData( name.get() , password.get() , SendEmail.get() , number.get())
    scrape=code()
    internet_connection = scrape.internet() 
    Gmail_Status=send.login_check()
    if internet_connection == True:
        if Gmail_Status == 'Login Successful':
            status = Label(tab1, text=Gmail_Status ,bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            x=messagebox.showinfo(message=  Gmail_Status )
            if x=='ok':
                status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

                
        elif Gmail_Status == 'Login Failed':
            status = Label(tab1, text=Gmail_Status ,bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            x=messagebox.showerror("Error", 'Please Check Name,Password & Enabling Third Party at Gmail')
            if x=='ok':
                status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
    else:
        status = Label(tab1, text="Please check the internet connection" ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
        x=messagebox.showinfo(message= "Please check the internet connection" )
        if x=='ok':
            status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")



action1 = ttk.Button(tab1,text = "Connect" ,command= ClickAction2 ).grid(column = ButtonCol, row = row)







# Frame 3
row+=1

#label Send To
aLabel = ttk.Label(tab1 , text = 'Send To:')
aLabel.grid(column = 0, row = row , columnspan=1, sticky="we")


row+=1
#FieldText Send To
#global SendEmail
SendEmail = tk.StringVar()
SendEmailEntered = ttk.Entry(tab1,width=12,textvariable=SendEmail)
SendEmailEntered.grid(column=0,row = row , columnspan=2, sticky="we")
if file_store !=[0,0," "," "," "]:
    SendEmailEntered.insert(0, file_store[4])
else :
    SendEmailEntered.insert(0,'')





#CheckBox Keep




Keep2 = tk.IntVar()
Keep2check1 = tk.Checkbutton(tab1, text = "Keep" , variable = Keep2 )
Keep2check1.grid(column = 3, row = row, sticky = tk.W)
if file_store[1] == '1':
    Keep2check1.select()

#Button Check


def ClickAction3():
    scrape=code()
    internet_connection = scrape.internet() 
    if internet_connection == True :
        scrape=code()
        idf=wine_list[str(number.get())]
        #print(scrape.check_files_number())
        status_key = idf in scrape.check_files_number()
        #print(status_key)
        if status_key == True:
            send=sendData( name.get() , password.get() , SendEmail.get() , number.get())

        #user               = 'samir.ahmed.abdelazem@gmail.com'
        #password           ='123456789asd!@#'
        #sendto             = 'samir.ahmed.abdelazem@gmail.com'
        #user               = name.get()
        #password1           = password.get()
        #sendto             = SendEmail.get()

    ##    try:    
        #ahmed.email_send(user,password,sendto)
            if chVarUn.get() == 0:
                send.email_send()
                status = Label(tab1, text="Email Send with Excel.",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
                x=messagebox.showinfo(message= "Email Send with "+str(idf)+"-"+str(number.get())+" Excel File.")
                if x=='ok':
                    status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                    status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")


            elif chVarUn.get() == 1:
                send.email_send_two_attachments()
                status = Label(tab1, text="Email Send with Excel & json.",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
                x=messagebox.showinfo(message= "Email Send with "+str(idf)+"-"+str(number.get())+" Excel & json Files.")
                if x=='ok':
                    status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                    status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

        ##    except:
        ##        status = Label(tab1, text="Enter Email & Password.",bd=1 , relief =SUNKEN , anchor=W )
        ##        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")

        else:
            status = Label(tab1, text="Please Scrape First.",bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
            x=messagebox.showinfo(message= 'Please Scrape First')
            if x=='ok':
                status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
                status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")


    else:
        status = Label(tab1, text="Please check the internet connection" ,bd=1 , relief =SUNKEN , anchor=W )
        status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")
        x=messagebox.showinfo(message= "Please check the internet connection" )
        if x=='ok':
            status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
            status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")





action3 = ttk.Button(tab1,text = "SEND" ,command=ClickAction3).grid(column = ButtonCol, row = row)





row+=1
# Frame 4
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(tab1, text = "Excel" , variable = chVarDis, state = 'disabled')
check1.select()
check1.grid(column = 0, row = row, sticky = tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(tab1, text = 'Json', variable = chVarUn)
check2.deselect()
check2.grid(column =  1, row = row, sticky=tk.N)





#Frame Status
status = Label(tab1, text="Ready...    ",bd=1 , relief =SUNKEN , anchor=W )
status.grid(row=Statusrow, column=0, columnspan=Statuscolumnspan, sticky="we")




#Exit
def protocolhandler():
    x=messagebox.askokcancel("Exit", "Wanna leave?")
    if x == True:
        if Keep1.get() == 1 and Keep2.get() == 1 :
            write=['1','1',name.get(),password.get(),SendEmail.get()]
        elif Keep1.get() == 0 and Keep2.get() == 1 :
            write=['0','1','','',SendEmail.get()]
        elif Keep1.get() == 1 and Keep2.get() == 0 :
            write=['1','0',name.get(),password.get(),'']
        elif Keep1.get() == 0 and Keep2.get() == 0 :
            write=['0','0','','','']
        print('write',write)
        with open('data.pickle', 'wb') as f:
            pickle.dump(write, f, pickle.HIGHEST_PROTOCOL)
        win.destroy()

win.protocol("WM_DELETE_WINDOW", protocolhandler)
win.mainloop()



##
##def gmail( ):
##    usermail = user_email.get()
##    receivermail=receiver_email.get()           
##    server=smtplib.SMTP('smtp.gmail.com:587')
##    pass_word=password.get()
##    subject=subj.get()
##    #This allow you to include a subject by adding from, to and subject 
##    line
##    main_message=body.get('1.0', 'end-1c')
##    Body="""From: Name here <usermail>
##    To: <receivermail>
##    Subject:%s 
##
##    %s
##    """ %(subject,main_message )
##    try:
##        server=smtplib.SMTP('smtp.gmail.com:587')
##        server.ehlo()
##        server.starttls()
##        server.login(usermail, pass_word  )
##        server.sendmail(usermail,receivermail, Body )
##
##        text.insert(1.0, 'message sent')
##        #error handling
##    except  (smtplib.SMTPException,ConnectionRefusedError,OSError):
##        text.insert(1.0, 'message not sent')
##    finally:server.quit()




#try
#group = LabelFrame(win, text="Group", bd=1,padx=5, pady=5)
#group.grid(row=9, column=0, columnspan=3, sticky="we")




##import pickle
##
##
##def  pickle_store(array, status):
##    if status == 'w':
##        output = open('klwines.pkl', 'wb')
##        pickle.dump(list, output)
##        output.close()
##    elif status == 'r':
##        pkl_file = open('klwines.pkl', 'rb')
##        data1 = pickle.load(pkl_file)
##        pkl_file.close()
##        return data1


##scores = {} # scores is an empty dict already
##target='klwines.packle'
##if os.path.getsize(target) > 0:      
##    with open(target, "rb") as f:
##        try:
##            unpickler = pickle.Unpickler(f)
##            # if file is not empty scores will be equal
##            # to the value unpickled
##            scores = unpickler.load()
##        except EOFError:
##            scores = list()  # or whatever you want
##
###print(scores[0])
##print(scores)

#with open ('klwines.pkl', 'rb') as pickel_file :
  #  new_data=pickle.load(pickel_file)
 #   print(new_data)

#print(new_data[1])
##
##save_data = { 1 : Keep1.get() , 2: Keep1.get(), 3 : name.get() , 4 : password.get() , 5: SendEmail.get()}
##
##pickle_out = open('klwines.pickle', 'wb')
##pickle.dump(save_data,pickle_out )
##pickle_out.close
##store= pickle_store(save_data , 'w')





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
