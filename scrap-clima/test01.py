# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 13:38:06 2021

@author: UniverSapphireLotus
"""

import urllib.request
from bs4 import BeautifulSoup
url= 'https://www.accuweather.com/es/pe/ayacucho/257014/january-weather/257014?year=2021'




data= urllib.request.urlopen(url)
print(data.read().decode())

soup= BeautifulSoup(data)
tags= soup('a')
'''
for tag in tags:
    print(tag.get('href'))

'''
