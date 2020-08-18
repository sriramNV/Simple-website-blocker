""" Remember, run this file with ADMINISTRTOR ACCESS since it modifies the system file."""


import time
from datetime import datetime as dt


#hosttemp = "host_list.txt"  #just a temporary host while coding since i don't wanted to work on actual system file


hostPath=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"

#add sites that you want to block
websiteList = ["www.facebook.com","facebook.com"]

#for writing websites that are needed to be blocked while office hours
while True:
    if dt.now().hour >= 8 and dt.now().hour <= 16:
        with open(hostPath,'r+') as file:
            content = file.read()
            print(content)
            for website in websiteList:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
  #for removing the websites from block list after office hours, seriously i don't know when is your office hours so modify it yourself.  
    else:
        with open(hostPath,'r+') as file:
            content = file.readline()
            file.seek(0)
            for line in content:
                if not any(website in line for website in websiteList):
                    file.write(line)
            file.truncate()


    time.sleep(60)