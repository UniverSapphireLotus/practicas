# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:01:01 2021

@author: UniverSapphireLotus


"""
soup = BeautifulSoup(plateRequest.text)
#print(soup.prettify())
#print soup.find_all('tr')

table = soup.find("table", { "class" : "lineItemsTable" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    print cells