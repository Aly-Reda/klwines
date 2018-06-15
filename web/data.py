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
#from web.get import scrape as code 

class compare:
    
    def __init__(self):
        pass

    def get_data_identifier(identifier):
        identifier_id=identifier
        wine_list={ 7:'Beer' ,10:'Distilled Spirits' ,0:'Other',23:'Sake',15:'Soda' ,5:'Wine - Dessert',1:'Wine - Red' ,3:'Wine - Rose' ,4:'Wine - Sparkling' ,2:'Wine - White'}
        identifier_Name=wine_list[identifier]
        return identifier_id , identifier_Name

    def Excel ():
        file1,file2= code.latest_two_Excel()
        dataFrame1 = pd.read_excel(str(file1))
        data1=len(dataFrame1.iloc[:,0]) 
        dataFrame2 = pd.read_excel(str(file2))
        data2=len(dataFrame2.iloc[:,0])
        if data1 == data2:
            df1 = pd.read_excel(str(file1))
            df2 = pd.read_excel(str(file2))
            difference = df1[df1!=df2]    
            xnr = difference.notnull().values.any()
            if xnr == False:
                flage=2
            else:
                flage=1
        else:
            flage=0

        return flage



    def base_email():
        base = compare.Excel()
        ident_id ,fileiden_name = compare.get_data_identifier()
        subject = 'Scraping Klwines Website '+ident_id+"-"+fileiden_name
        if base == 0 :
            
            body = ident_id+"-"+fileiden_name+' count: '+str(code.Page_Count(1,ident_id))+"\nStatus: Data Increament"
            html1="<h3 style='color: blue;'>"+str(body.replace("\n","<br>"))+"</h3>"

            
            html2="<h3 style='color: blue;'>"+str(body.split('\n')[1])+"</h3>"
        elif base ==1 :
            body = ident_id+"-"+fileiden_name+' count: '+str(code.Page_Count(1,ident_id))+"\nStatus: Data Updated"
            html1="<h3 style='color: blue;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==2 :
            body = ident_id+"-"+fileiden_name+' count: '+str(code.Page_Count(1,ident_id))+"\nStatus: Same Data"
            html1="<h3 style='color: blue;'>"+str(body.replace("\n","<br>"))+"</h3>"
        return subject,body,html1







##    def txt(file,flage,number=0):
##        if flage == 'w': 
##            f = open(file,'w').write(number)
##        
##        elif flage == 'r':
##            k = open(file, 'r').read()
##            return str(k)
##        elif flage == 'rl':
##            f=[line.rstrip('\n') for line in open(str(file))]
##            return f


