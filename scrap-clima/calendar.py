# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 06:41:18 2021

@author: UniverSapphireLotus
"""
import pandas as pd
yy=2021

# display the calendar
sun=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SUN').strftime('%Y-%m-%d').tolist()

print(sun)

sat=pd.date_range(start=str(yy), end=str(yy+1), freq='W-SAT').strftime('%Y-%m-%d').tolist()
print(sat)


for i in sat:
    print(i)