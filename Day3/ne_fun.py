import os
import datetime #new library

def run_command(command):  #defining function
    return os.system(command)

def show_date():
    return datetime.datetime.today() #define the function

# run_command("date")
# run_command("df -h")       #calling function

today = show_date() #call the function
print(today)