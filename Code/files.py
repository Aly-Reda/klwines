import os
import glob
class give:
    def __init__(self) :
        pass
    def latest_one_file(self):
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\Files'+r'\\'
        files_path = os.path.join(folder, '*.xlsx')
        files = sorted(glob.iglob(files_path), key=os.path.getctime, reverse=True)
        Excel_Path = "files\\"+files[0].split('\\')[-1]
        Excel_name =files[0].split('\\')[-1]
        return Excel_Path ,Excel_name

    def latest_two_files(self):
        cwd = os.getcwd()
        folder=cwd.replace('\\','\\\\')+r'\\Files'+r'\\'
        files_path1 = os.path.join(folder, '*.xlsx')
        files_path2 = os.path.join(folder, '*.json')
        Excel = sorted(glob.iglob(files_path1), key=os.path.getctime, reverse=True)
        json  = sorted(glob.iglob(files_path2), key=os.path.getctime, reverse=True)
        Excel_Path = "Files\\"+Excel[0].split('\\')[-1]
        Excel_name=Excel[0].split('\\')[-1]
        Json_Path  = "Files\\"+json[0].split('\\')[-1]
        Json_name=json[0].split('\\')[-1]
        return  Excel_Path, Json_Path ,Excel_name ,Json_name
