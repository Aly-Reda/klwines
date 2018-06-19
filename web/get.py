import datetime
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import os
import glob
import socket

class scrape:
    
    def __init__(self, identifier =10 ) :
        self.identifier=identifier 
        wine_list={ 7:'Beer' ,10:'Distilled Spirits' ,0:'Other',23:'Sake',15:'Soda' ,5:'Wine - Dessert',1:'Wine - Red' ,3:'Wine - Rose' ,4:'Wine - Sparkling' ,2:'Wine - White'}
        self.identifier_value= wine_list[self.identifier]


    def row(self , Page):
        url="http://www.klwines.com/productfeed?&productTypeCD="+str(self.identifier)+"&minprice=&maxprice=&page="+str(Page)
        row_blocks = BeautifulSoup(requests.get(url).text, 'html.parser').findAll('tr')
        return row_blocks


    #Scrape Text & href
    def col(self ,row_one_block , col_number , status):
        if status == 'txt':
            try:
                col_text=row_one_block.findAll('td')[int(col_number)].getText().strip(" \n\t\r")
                return col_text
            except:
                col_text=""
                return col_text
        elif status == 'href':
            try:
                t=row_one_block.findAll('td')[int(col_number)]
                t2=t.findAll('a')[0]['href']
                col_href="https://www.klwines.com"+str(t2)
                return col_href
            except:
                col_href=""
                return col_href


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
