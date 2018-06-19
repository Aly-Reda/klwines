import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from web.get import scrape as code
class get:
    
    def __init__(self , User_Email , User_Password , Send_To , identifier_value ):
        #self.User_Email = User_Email
        #self.User_Password = User_Password
        #self.Send_To = Send_To
        #self.identifier_value=identifier_value 
        #wine_list={ 'Beer':7 ,'Distilled Spirits':10 ,'Other':0,'Sake':23,'Soda':15 ,'Wine - Dessert':5,'Wine - Red':1 ,'Wine - Rose':3 ,'Wine - Sparkling':4 ,'Wine - White':2}
        #self.identifier= wine_list[self.identifier_value]
