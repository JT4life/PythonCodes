import requests
from bs4 import BeautifulSoup
#command prompt pip install requests, bs4 (beautiful package)
webpage = requests.get("http://www.yahoo.com")
print(webpage.text)


getpage=requests.get("http://www.yahoo.com")
x=BeautifulSoup(getpage.text, 'html.parser')
all_links=x.findAll('a')
for link in all_links:
   print(link)
	
#import subprocess calc notepad

import subprocess
subprocess.Popen("calc.exe")

#import pyautogui (used for gui operations)

import pyautogui
'''pic=pyautogui.screenshot()
pic.save('screenshot.jpg')'''

pyautogui.moveTo(300,300,duration=0.5) #moves mouse cursor

import webbrowser
webbrowser.open("http://www.yahoo.com")

#open a word.doc file

