import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from web.get import scrape as code
from web.files import give as file

class get:
    
    def __init__(self , User_Email , User_Password , Send_To , identifier_value ):
        self.User_Email = User_Email
        self.User_Password = User_Password
        self.Send_To = Send_To
        self.identifier_value=identifier_value 
        wine_list={ 'Beer':7 ,'Distilled Spirits':10 ,'Other':0,'Sake':23,'Soda':15 ,'Wine - Dessert':5,'Wine - Red':1 ,'Wine - Rose':3 ,'Wine - Sparkling':4 ,'Wine - White':2}
        self.identifier= wine_list[self.identifier_value]


    def email_send(self):
        get_file=file(self.identifier)
        filename , excel_name = get_file.latest_one_file()
        subject,body,html1  = get_file.base_email()
        msg = MIMEMultipart()
        msg['From'] = self.User_Email
        msg['To'] = self.Send_To
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))
        msg.attach(MIMEText(html1, 'html'))
        attachment  =open(filename,'rb')
        part = MIMEBase('application','octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',"attachment; filename= "+excel_name)
        msg.attach(part)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login( self.User_Email ,self.User_Password)
        server.sendmail( self.User_Email , self.Send_To ,text)
        print(str(subject)+' Excel File Attached\nEmail Send Successfully')
        server.quit()

    def email_send_two_attachments(self):
        convert=code(self.identifier)
        get_file=file(self.identifier)

        try:
            filename1,filename2 , excel_name,jason_name=get_file.latest_two_files()
        except:
            convert.json()
            filename1,filename2 , excel_name,jason_name=get_file.latest_two_files()
        subject,body,html1  =get_file.base_email()
        msg = MIMEMultipart()
        msg['From'] = self.User_Email
        msg['To'] = self.Send_To
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'plain'))
        msg.attach(MIMEText(html1, 'html'))
        attachment1  =open(filename1,'rb')
        part1 = MIMEBase('application','octet-stream')
        part1.set_payload((attachment1).read())
        encoders.encode_base64(part1)
        part1.add_header('Content-Disposition',"attachment; filename= "+excel_name)
        msg.attach(part1)
        attachment2  =open(filename2,'rb')
        part2 = MIMEBase('application','octet-stream')
        part2.set_payload((attachment2).read())
        encoders.encode_base64(part2)
        part2.add_header('Content-Disposition',"attachment; filename= "+jason_name)
        msg.attach(part2)
        text = msg.as_string()
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(self.User_Email, self.User_Password)
        server.sendmail( self.User_Email , self.Send_To , text)
        print(str(subject)+' Excel & Json Files Attached\nEmail Send Successfully')
        server.quit()










##    def email_send_three_attachments(email_user,email_password,email_send,subject,body,html1,html2,filename1,filename2,filename3):
##        #filename1,filename2 , excel_name,jason_name=code.latest_two_files()
##        subject,body,html1  =code.base_email()
##        #print(excel_name)
##        #print(jason_name)
##        msg = MIMEMultipart()
##        msg['From'] = email_user
##        msg['To'] = email_send
##        msg['Subject'] = subject
##        msg.attach(MIMEText(body,'plain'))
##        msg.attach(MIMEText(html1, 'html'))
##
##        attachment1  =open(filename1,'rb')
##        part1 = MIMEBase('application','octet-stream')
##        part1.set_payload((attachment1).read())
##        encoders.encode_base64(part1)
##        part1.add_header('Content-Disposition',"attachment; filename= "+filename1)
##        msg.attach(part1)
##
##        attachment2  =open(filename2,'rb')
##        part2 = MIMEBase('application','octet-stream')
##        part2.set_payload((attachment2).read())
##        encoders.encode_base64(part2)
##        part2.add_header('Content-Disposition',"attachment; filename= "+filename2)
##        msg.attach(part2)
##
##
##        attachment3  =open(filename3,'rb')
##        part3 = MIMEBase('application','octet-stream')
##        part3.set_payload((attachment3).read())
##        encoders.encode_base64(part3)
##        part3.add_header('Content-Disposition',"attachment; filename= "+filename3)
##        msg.attach(part3)
##
##        text = msg.as_string()
##        server = smtplib.SMTP('smtp.gmail.com',587)
##        server.starttls()
##        server.login(email_user,email_password)
##        server.sendmail(email_user,email_send,text)
##        print("Email Is Sent Successfully")
##        server.quit()
##
##
##


#import datetime
#import requests
#from bs4 import BeautifulSoup
#from openpyxl import Workbook
#import pandas as pd
#import xlrd
#import codecs
#import os
#import sqlite3
