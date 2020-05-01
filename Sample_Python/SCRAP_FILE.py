# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 15:46:31 2020

@author: Muhammed Hassan M
"""


import requests
import urllib.request
import time
from bs4 import BeautifulSoup
url = "https://rrcsearch3.neubus.com/esd3-rrc/index.php?_module_=esd&_action_=keysearch&profile=15"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
soup.findAll('table')
table = soup.findAll('table')[0]
link = one_a_tag['tr']
download_url = 'http://web.mta.info/developers/'+ link 
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:]) 
time.sleep(1)