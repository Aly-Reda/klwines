import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import xlrd
import codecs
import os
import sqlite3
from web.get import scrape as code

class get:
    
    def __init__(self):
        pass


    def login_check(user,password):
        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(user, password)
            Gmail_Status='Login Successful'
        except:  
            Gmail_Status='Login Failed'
        return Gmail_Status
    

    def email_send(email_user,email_password,email_send):
        try:
            filename , excel_name=code.latest_one_file()
        except:
            code.data()
            filename , excel_name=code.latest_one_file()
            
        subject,body,html1  =code.base_email()
        #print(filename)
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
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
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        print("Email Is Sent Successfully")
        server.quit()

    def email_send_two_attachments(email_user,email_password,email_send):
        try:
            filename1,filename2 , excel_name,jason_name=code.latest_two_files()
        except:
            code.data()
            code.json()
            filename1,filename2 , excel_name,jason_name=code.latest_two_files()
        subject,body,html1  =code.base_email()
        #print(excel_name)
        #print(jason_name)
        msg = MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
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
        server.login(email_user,email_password)
        server.sendmail(email_user,email_send,text)
        print("Email Is Sent Successfully")
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



