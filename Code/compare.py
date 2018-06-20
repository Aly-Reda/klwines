import pandas as pd
import os
import glob
from Code.get import scrape as code

class base:
    def __init__(self, identifier =10 ) :
        self.identifier=identifier 
        wine_list={ 7:'Beer' ,10:'Distilled Spirits' ,0:'Other',23:'Sake',15:'Soda' ,5:'Wine - Dessert',1:'Wine - Red' ,3:'Wine - Rose' ,4:'Wine - Sparkling' ,2:'Wine - White'}
        self.identifier_value= wine_list[self.identifier]


#identifierfirer
    def latest_two_Excel(self):
        one_file=''
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\Files'+r'\\'
        files_path = os.path.join(folder, str(self.identifier)+"-"+self.identifier_value+'*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        New_Excel = "Files\\"+files[0].split('\\')[-1]
        #if it is the first time the New_Excel and Old_Excel are the same
        try:
            Old_Excel = "Files\\"+files[1].split('\\')[-1]

        except:
            #base ==
            Old_Excel = New_Excel
            one_file='flage'
        #Excel_name =files[0].split('\\')[-1]
        #print('Latest Excel Created File Path Send')
        return Old_Excel , New_Excel , one_file



    def Excel_Compare(self):
        file1,file2 , one_file= self.latest_two_Excel()
        if one_file == 'flage':
            flage =4
            return flage
        dataFrame1 = pd.read_excel(str(file1))
        data1=len(dataFrame1.iloc[:,0]) 
        dataFrame2 = pd.read_excel(str(file2))
        data2=len(dataFrame2.iloc[:,0])
        #print(data1)
        if data1 == data2:       
            df1 = pd.read_excel(str(file1))
            df2 = pd.read_excel(str(file2))
            difference = df1[df1!=df2]    
            xnr = difference.notnull().values.any()
            if xnr == False:
                flage=0
                return flage

            else:
                flage=1
                return flage

        elif data1 < data2:
            flage=2
            return flage

        elif data1 > data2:
            flage=3
            return flage

# 0 Same Data
# 1 Data Updated
# 2 Increment 
# 3 decrement
# 4 first time

#identifierf
    def base_email(self):
        base = self.Excel_Compare()
        scrape=code(self.identifier)
        Page_Count_Number=scrape.Page_Count()
        subject = 'Scraping Klwines Website '+str(self.identifier)+"-"+self.identifier_value
        if base == 0 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(Page_Count_Number)+"\nStatus: Same Data"
            html1="<h3 style='color: black;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==1 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(Page_Count_Number)+"\nStatus: Data Updated"
            html1="<h3 style='color: blue;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==2 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(Page_Count_Number)+"\nStatus: Data Increment"
            html1="<h3 style='color: green;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==3 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(Page_Count_Number)+"\nStatus: Data Decrement"
            html1="<h3 style='color: red;'>"+str(body.replace("\n","<br>"))+"</h3>"
        elif base ==4 :
            body = str(self.identifier)+"-"+self.identifier_value+' count: '+str(Page_Count_Number)+"\nStatus: No Comparison First Time Scraping"
            html1="<h3 style='color: orange;'>"+str(body.replace("\n","<br>"))+"</h3>"

        return subject,body,html1




