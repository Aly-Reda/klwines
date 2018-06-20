import schedule
import time
from Code.get import scrape as code
from Code.send import get as Send_File

class Schedule:
    
    def __init__(self , User_Email , User_Password , Send_To ,Every_Minutes ):
        self.User_Email = User_Email
        self.User_Password = User_Password
        self.Send_To = Send_To
        self.Every_Minutes = Every_Minutes


    def schedule_time(self):
        schedule_status =schedule.every(self.Every_Minutes).minutes.do(self.scudling_scraping_email)
        print(schedule_status)
        while 1:
            schedule.run_pending()
            time.sleep(1)
            schedule_status='run_pending'
        return schedule_status
            

    def scudling_scraping_email (self):
        scrape=code(10)
        scrape.data()
        send = Send_File(self.User_Email , self.User_Password , self.Send_To ,'Distilled Spirits' )
        send.email_send()




##
##            #schedule.every().hour.do(job)
##       #schedule.every().day.at("10:30").do(job)
##        #schedule.every().hour.do(job)
##        #schedule.every().day.at("10:30")schedule.every(10).minutes.do(job)
##    def scudling_scraping (self):
##        scrape=code(self.identifier_value)
##        code.data()
##
##    def scudling_scraping_email (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send()
##  
##
##    def scudling_scraping_json (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##
##    def scudling_scraping_json_email (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send_two_attachments()
##
##
#####################################################################
##    def scudling_scraping_all (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send_two_attachments()
##
##    def scudling_scraping_all_json (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send_two_attachments()
##
##    def scudling_scraping_all_email (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send_two_attachments()
##
##    def scudling_scraping_all_json_email (self):
##        scrape=code(self.identifier_value)
##        code.data()
##        code.json()
##        send = Send_File(self.User_Email , self.User_Password , self.Send_To , self.identifier_value )
##        send.email_send_two_attachments()
