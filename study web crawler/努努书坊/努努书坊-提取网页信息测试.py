import requests
import bs4
from bs4 import BeautifulSoup
import re
import time

url = 'https://www.kanunu8.com/book2/11064/'
r = requests.get(url)
r.encoding='GBK'
html1 = r.text
soup = BeautifulSoup(html1,'html.parser')
t1 = soup.find('dd')
print(type(t1))
t2 = soup.find_all('dd')
print(type(t2))

for i in t2:
    print(i.string)
    print(i.contents)
    print(type(i.contents))
    a = str(i.contents)
    a = a.split("\"")
    a = str(a[1])
    print(a)

a = soup.find('a',href = '\d\d\d\d\d\d.html')
print(a)
