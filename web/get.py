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
import glob
#from web.data import compare as data

class scrape:
    
    def __init__(self):
        pass


    def row(Page,idfilter):
        url="http://www.klwines.com/productfeed?&productTypeCD="+str(idfilter)+"&minprice=&maxprice=&page="+str(Page)
        row_block = BeautifulSoup(requests.get(url).text, 'html.parser').findAll('tr')
        return row_block


    #Scrape Text
    def col(x , number , status):
        if status == 'txt':
            try:
                y=x.findAll('td')[int(number)].getText().strip(" \n\t\r")
                #print(y)
                return y

            except:
                y=""
                return y
        elif status == 'href':
            try:
                t=x.findAll('td')[int(number)]
                t2=t.findAll('a')[0]['href']
                y="https://www.klwines.com"+str(t2)
                return y
            except:
                y=""
                return y


    #Scrape Number of Pages
    def Page_Count(Page,idfilter):
        url="http://www.klwines.com/productfeed?&productTypeCD="+str(idfilter)+"&minprice=&maxprice=&page="+str(Page)
        count = BeautifulSoup(requests.get(url).text, 'html.parser').findAll('li', {'filter-id': str(idfilter)})[0]['count']
        return int(count)

    def Check_Connection():
        try:
            r = requests.get("http://www.klwines.com/productfeed?&productTypeCD=10&minprice=&maxprice=&page=1").status_code
            if r == 200:
                r='Website Working'
            else:
                 r='Website Down'

        except:
            r='No Internet Connection'
        return r



    def data(iden=10):
        cwd = os.getcwd()
        path=cwd.replace('\\','\\\\')+r'\files'        
        if not os.path.exists(path):
            os.makedirs(path)
        global ident
        ident=str(iden)
        wine_list={ 7:'Beer' ,10:'Distilled Spirits' ,0:'Other',23:'Sake',15:'Soda' ,5:'Wine - Dessert',1:'Wine - Red' ,3:'Wine - Rose' ,4:'Wine - Sparkling' ,2:'Wine - White'}
        global fileiden
        fileiden = wine_list[iden]
        wb = Workbook()
        ws = wb.active
        ws.append(["Date", "SKU", "Vintage","Item Name","Item URL","List Price","Quantity On Hand","Allocation"])
        outof=(scrape.Page_Count(1,iden)//50)+2
        current_page  = 1
        while current_page < outof:
            #print(str(current_page)+" out of "+str(outof-1))
            for x in scrape.row(current_page,iden):
                td1=scrape.col(x ,0 , 'txt')
                td2=scrape.col(x ,1 , 'txt')
                td3=scrape.col(x ,2 , 'txt')
                td4=scrape.col(x ,3 , 'txt')
                td5=scrape.col(x ,3 , 'href')
                td6=scrape.col(x ,4 , 'txt')
                td7=scrape.col(x ,5 , 'txt')
                td8=scrape.col(x ,6 , 'txt')
                if td1!="" and td1!="No results with filters selected.":
                
                    ws.append([ td1, td2 , td3 , td4 , td5 , td6 , td7 , td8 ])
                else:
                    pass
            current_page+=1
        print('Data Scraped Successfully')
        wb.save("files\\"+ident+"-"+fileiden+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".xlsx")
        print('Data Store in Excel Formate Successfully')
        return str(iden)
        
        
    def json():
        try:
            pd.read_excel("files\\"+ident+"-"+fileiden+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".xlsx").to_json("files\\"+ident+"-"+fileiden+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".json")
            print('Data Store in Json Formate Successfully by Methode One')

        except:
            pd.read_excel(scrape.latest_one_file()).to_json(scrape.latest_one_file().replace(".xlsx",".json"))
            print('Data Store in Json Formate Successfully by Methode Two')


    def latest_one_file():
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path = os.path.join(folder, '*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        Excel_Path = "files\\"+files[0].split('\\')[-1]
        Excel_name =files[0].split('\\')[-1]
        print('Latest Excel Created File Path Send')
        return Excel_Path ,Excel_name 

    def latest_two_files():
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\files'  
        files_path1 = os.path.join(folder, '*.xlsx')
        files_path2 = os.path.join(folder, '*.json')
        Excel = sorted(glob.iglob(files_path1), key=os.path.getctime, reverse=True)
        json  = sorted(glob.iglob(files_path2), key=os.path.getctime, reverse=True)
        Excel_Path = "files\\"+Excel[0].split('\\')[-1]
        Excel1=Excel[0].split('\\')[-1]
        Json_Path  = "files\\"+json[0].split('\\')[-1]
        Json1=json[0].split('\\')[-1]
        print('Latest Excel & Json Created File Path Send')
        return  Excel_Path, Json_Path ,Excel1 ,Json1

    def latest_two_Excel():
        cwd = os.getcwd()
        identires,fileideniers=data.get_data_identifier()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path = os.path.join(folder, identires+"-"+fileideniers+'*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        New_Excel = "files\\"+files[0].split('\\')[-1]
        #if it is the first time the New_Excel and Old_Excel are the same
        try:
            Old_Excel = "files\\"+files[1].split('\\')[-1]
        except:
            Old_Excel = "files\\"+files[0].split('\\')[-1]
        #Excel_name =files[0].split('\\')[-1]
        #print('Latest Excel Created File Path Send')
        return Old_Excel , New_Excel
