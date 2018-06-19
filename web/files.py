import datetime
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import pandas as pd
import os
import glob
import socket
from web.get import scrape as code

class give:
    def __init__(self) :
        pass
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




