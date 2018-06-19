import requests
import os
import glob
import socket
import smtplib

class valid:
    
    def __init__(self , User_Email='' , User_Password=''):
        self.User_Email = User_Email
        self.User_Password = User_Password


    def Internet_Connection (self):
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




    def Website_Connection(self):
        try:
            r = requests.get("http://www.klwines.com/productfeed?&productTypeCD=10&minprice=&maxprice=&page=1").status_code
            if r == 200:
                r='Website Working'
            else:
                 r='Website Down'

        except:
            r='No Internet Connection'
        return r

    def Gmail_Login(self):
        #print(self.User_Email)
        #print(self.User_Password)
        try:  
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()

            server.login( self.User_Email , self.User_Password )
            Gmail_Status='Login Successful'
        except:  
            Gmail_Status='Login Failed'
        return Gmail_Status



    def Files_Found(self):
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







