import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import schedule
import time
from web.get import scrape as code
from web.files import give as file
from web.compare import base
from web.send import get as Send_File

class get:
    
    def __init__(self , User_Email , User_Password , Send_To , identifier_value ):
        self.User_Email = User_Email
        self.User_Password = User_Password
        self.Send_To = Send_To
        self.identifier_value=identifier_value 
        wine_list={ 'Beer':7 ,'Distilled Spirits':10 ,'Other':0,'Sake':23,'Soda':15 ,'Wine - Dessert':5,'Wine - Red':1 ,'Wine - Rose':3 ,'Wine - Sparkling':4 ,'Wine - White':2}
        self.identifier= wine_list[self.identifier_value]

    #def job():
     #   print("I'm working...")
    def schedule_time():
        schedule.every(10).minutes.do(job)
        schedule.every().hour.do(job)
        schedule.every().day.at("10:30").do(job)
        
        schedule.every().hour.do(job)
        schedule.every().day.at("10:30")schedule.every(10).minutes.do(job)

        while 1:
            schedule.run_pending()
            time.sleep(1)

    def scudling_scraping (self):
        scrape=code(self.identifier_value)
        code.data()

    def scudling_scraping_email (self):
        scrape=code(self.identifier_value)
        code.data()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send()
  

    def scudling_scraping_json (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()

    def scudling_scraping_json_email (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send_two_attachments()


###################################################################
    def scudling_scraping_all (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send_two_attachments()

    def scudling_scraping_all_json (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send_two_attachments()

    def scudling_scraping_all_email (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send_two_attachments()

    def scudling_scraping_all_json_email (self):
        scrape=code(self.identifier_value)
        code.data()
        code.json()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
        send.email_send_two_attachments()
