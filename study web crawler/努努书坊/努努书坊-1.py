import requests
import bs4
from bs4 import BeautifulSoup
import re


def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='GBK'
        print(r.text)
        return r.text
        
    except:
        print('爬取失败')


def message(html):
    soup=BeautifulSoup(html,'html.parser')
    all_t=soup.find_all('title')
    t = str(all_t).split('>')
    t = t[1].split('_',maxsplit=1)
    tt =  str(t[0])
    print(tt)
    all_p=soup.find_all('p')
    s = str(all_p)

    while True:                      #用换行符替换所有的'<br/>'
        index_begin = s.find("<")
        index_end = s.find(">",index_begin + 1)
        if index_begin == -1:
            break
        s = s.replace(s[index_begin:index_end+1],"\n")

    ss = tt + '\n' +s[1:-1]

    print(ss)

    return ss
    

url='https://www.kanunu8.com/book/3813/38503.html'
html=getHTML(url)
parseWeb=message(html)
