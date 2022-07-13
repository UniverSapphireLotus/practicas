import requests
from bs4 import BeautifulSoup
r = requests.get('https://dynasty-scans.com/series/citrus')
soup = BeautifulSoup(r.text, 'lxml')