# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 21:54:10 2018

@author: Jay
"""

#Imports
from datetime import datetime as dt

# r is added for passing the entire path as row string so that special character effect can be nullified
#I have used temp path to avoid any accident. When you use real hostfile path i.e. C:\Windows\System32\drivers\etc\hosts, make sure to keep a backup of the original host file.

hosts_path_temp=r"path\hosts"
redirect="127.0.0.1"
website_list=['www.facebook.com', 'facebook.com', 'www.gmail.com', 'gmail.com']

while True: # to keep the loop running
# check if current time is in working hour
if dt(dt.now().year, dt.now().month, dt.now().day,8) < (dt.now()) < dt(dt.now().year, dt.now().month, dt.now().day,18):
    print('Working hour..')
    with open(hosts_path_temp, 'r+') as file:
        content = file.read()
        for website in website_list:
            if website in content:
                pass
            else:
                file.write(redirect + " "+ website+"\n")
    
else:
    print('Fun hour..')
    with open(hosts_path_temp, 'r+') as file:
        content=file.readlines()
        file.seek(0) # move the cursor to start of file
        for line in content:
            if not any (website in line for website in website_list):
                file.write(line)
        file.truncate() # delete all after the file updated as per above loop