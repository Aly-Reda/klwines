import datetime
import requests
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
import glob
import time
import socket

class scrape:
    
    def __init__(self, identifier =10 ) :
        self.identifier=identifier 
        wine_list={ 7:'Beer' ,10:'Distilled Spirits' ,0:'Other',23:'Sake',15:'Soda' ,5:'Wine - Dessert',1:'Wine - Red' ,3:'Wine - Rose' ,4:'Wine - Sparkling' ,2:'Wine - White'}
        self.identifier_value= wine_list[self.identifier]


    def row(self , Page):
        url="http://www.klwines.com/productfeed?&productTypeCD="+str(self.identifier)+"&minprice=&maxprice=&page="+str(Page)
        row_block = BeautifulSoup(requests.get(url).text, 'html.parser').findAll('tr')
        return row_block


    #Scrape Text & href
    def col(self ,x , number , status):
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


    #Scrape Number of items
    def Page_Count(self):
        url="http://www.klwines.com/productfeed?&productTypeCD="+str(self.identifier)+"&minprice=&maxprice=&page=1"
        count = BeautifulSoup(requests.get(url).text, 'html.parser').findAll('li', {'filter-id': str(self.identifier)})[0]['count']
        return int(count)



    def data(self):
        cwd = os.getcwd()
        path=cwd.replace('\\','\\\\')+r'\files'        
        if not os.path.exists(path):
            os.makedirs(path)
        wb = Workbook()
        ws = wb.active
        ws.append(["Date", "SKU", "Vintage","Item Name","Item URL","List Price","Quantity On Hand","Allocation"])
        outof=(self.Page_Count()//50)+2
        current_page  = 1
        while current_page < outof:
            print(str(current_page)+" out of "+str(outof-1))
            for x in self.row(current_page):
                td1=self.col(x ,0 , 'txt')
                td2=self.col(x ,1 , 'txt')
                td3=self.col(x ,2 , 'txt')
                td4=self.col(x ,3 , 'txt')
                td5=self.col(x ,3 , 'href')
                td6=self.col(x ,4 , 'txt')
                td7=self.col(x ,5 , 'txt')
                td8=self.col(x ,6 , 'txt')
                if td1!="" and td1!="No results with filters selected.":
                
                    ws.append([ td1, td2 , td3 , td4 , td5 , td6 , td7 , td8 ])
                else:
                    pass
            current_page+=1
        wb.save("files\\"+str(self.identifier)+"-"+self.identifier_value+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".xlsx")
        print('scrape done and file saved')        
        
    def json(self):
        try:
            pd.read_excel("files\\"+self.identifier+"-"+self.identifier_value+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".xlsx").to_json("files\\"+identifier+"-"+identifier_value+" "+str(datetime.datetime.now().strftime("[%H.%M] [%d-%m-%Y]"))+".json")
        except:
            file = self.latest_one_file()[0]
            file2=file.replace(".xlsx",".json")
            pd.read_excel(file).to_json(file2)

    def latest_one_file(self):
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path = os.path.join(folder, '*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        Excel_Path = "files\\"+files[0].split('\\')[-1]
        Excel_name =files[0].split('\\')[-1]
        return Excel_Path ,Excel_name 

    def latest_two_files(self):	
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path1 = os.path.join(folder, '*.xlsx')
        files_path2 = os.path.join(folder, '*.json')
        Excel = sorted(glob.iglob(files_path1), key=os.path.getctime, reverse=True)
        json  = sorted(glob.iglob(files_path2), key=os.path.getctime, reverse=True)
        Excel_Path = "files\\"+Excel[0].split('\\')[-1]
        Excel1=Excel[0].split('\\')[-1]
        Json_Path  = "files\\"+json[0].split('\\')[-1]
        Json1=json[0].split('\\')[-1]
        return  Excel_Path, Json_Path ,Excel1 ,Json1



#identifierfirer
    def latest_two_Excel(self):
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path = os.path.join(folder, str(self.identifier)+"-"+self.identifier_value+'*.xlsx')
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




    def Excel_Compare(self):
        file1,file2= self.latest_two_Excel()
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

#identifierf
    def base_email(self ):
        base = self.Excel_Compare()
        subject = 'Scraping Klwines Website '+str(self.identifier)+"-"+self.identifier_value
        if base == 0 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(self.Page_Count())+"\nStatus: Data Decrement or Increment"
            html1="<h3 style='color: green;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==1 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(self.Page_Count())+"\nStatus: Data Updated"
            html1="<h3 style='color: blue;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==2 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(self.Page_Count())+"\nStatus: Same Data"
            html1="<h3 style='color: black;'>"+str(body.replace("\n","<br>"))+"</h3>"
        return subject,body,html1



    def internet (self):
      REMOTE_SERVER = "www.google.com"
      try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(REMOTE_SERVER)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        return True
      except:
         pass
      return False






    def Check_Connection(self):
        try:
            r = requests.get("http://www.klwines.com/productfeed?&productTypeCD=10&minprice=&maxprice=&page=1").status_code
            if r == 200:
                r='Website Working'
            else:
                 r='Website Down'

        except:
            r='No Internet Connection'
        return r

    def check_files_number(self):
        list1 = []
        new=[]
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\files'+r'\\'
        files_path = os.path.join(folder,'*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        if len(files[:]) > 0:
            for i in files:
                list1.append(i.split('\\')[-1].split(' [')[0])
                seen = set()
                seen_add = seen.add
                files_name =[x for x in list1 if not (x in seen or seen_add(x))]
                #print(files_name)
            for x in files_name:
                new.append(int(x.split('-')[0]))
        #the first run of the app when we have no files folder
        else:
            new = [1000 , 2000]            
        return sorted(new)











