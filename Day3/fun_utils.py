import os

command = "df -h" #disk
command = "uptime" #load average
command = "date" #date  #will print only value of date
print(os.system(command))

#to counter this we will learn functions

def check_cpu(command):
    print(os.system(command))

def check_date(command): #defining a function
    print(os.system(command))

check_cpu("df -h") #calling a function

check_date("uptime")