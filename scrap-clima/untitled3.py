# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 18:27:54 2021

@author: UniverSapphireLotus
"""

import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from requests_toolbelt.utils import dump

#url= 'https://www.accuweather.com/es/pe/ayacucho/257014/january-weather/257014?year=2021'
url= 'https://www.wunderground.com/history/daily/pe/ayacucho/SPHO/date/2021-10-20'


#url='http://www.estesparkweather.net/archive_reports.php?date=202005'

response = requests.get(url)

print(response)


#data = dump.dump_all(response)
#data.decode('utf-8')
#print(data.decode('utf-8'))
time.sleep(5)

soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.prettify())

data = []
time.sleep(5)
#table = soup.find('table', attrs={'class':'_ngcontent-app-root-c204'})
#table = soup.find('div', attrs={'id':'dpr_manager'})

table = soup.find('router-outlet')
table = soup.find('app-history')

#print(table)
#for each_div in soup.findAll('table',{'class':'row'}):
#for each_div in soup.findAll('div',{'class':'observation-table ng-star-inserted'}):
#for each_div in soup.findAll('table',{'class':'mat-footer-row cdk-footer-row ng-star-inserted'}):
#for each_div in soup.findAll("div", {"id": "articlebody"}):

#for each_div in soup.find('app-history'):
#for each_div in soup.findAll('div', {'class': 'row'}):

#for each_div in soup.findAll('div', {'class': 'small-12 columns has-sidebar'}):
time.sleep(1)   
time.sleep(5)

for each_div in soup.findAll('lib-city-history-observation'):
#for each_div in soup.findAll('div', {'class': 'observation-title'}):
#for each_div in soup.findAll('div', {'class': 'observation-table ng-star-inserted'}):
    print (each_div)
    
'''
rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele]) # Get rid of empty values
'''