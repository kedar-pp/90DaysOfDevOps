# python libraries-----
#                     |--> OS (operating sys library)
#                     |--> shutil (shell utlis)
#                     |--> system (sys level)


# Importing a library for os
import os 

# linuc cmd to see diskspace i.e df -h
print(os.system('df -h'))

# we can see kab se sys chalu hey i.e uptime and load average

print(os.system('uptime')) #for linux and mac 


print(os.system('systeminfo')) #for windows

print(os.system('sysctl hw.memsize')) #for linux and mac RAM
