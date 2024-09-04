import shutil
import datetime
import os

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz")  
    
    #before backuping we have to compress the 200mb file neither for 10 days it wil backuped for 2gb .tar.gz is compres extenstion
    #agar kise be formatted string ke betch me string lagana hota hey to f use karte hai

    shutil.make_archive(backup_file_name,'gztar',source)

source = "/Users/kedar/OneDrive/Desktop/tws/90DaysOfDevOps"
destination ="/Users/kedar/OneDrive/Desktop/tws/90DaysOfDevOps/mini_project"
backup_files(source,destination)