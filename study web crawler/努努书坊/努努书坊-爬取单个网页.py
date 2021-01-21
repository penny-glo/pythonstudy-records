import requests
import bs4
from bs4 import BeautifulSoup
import re
import time


def getHTML(url):  #爬取网页
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='GBK'
        return r.text
    except:
        print('爬取失败')


def message(html):  #解析网页，获取所有小说内容
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


def txt(parseWeb):  #保存为txt文件
    with open("C:\\Users\\mac\\Desktop\\后宫·甄嬛传\\番外4.txt",'a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


#主程序
with open("C:\\Users\\mac\\Desktop\\后宫·甄嬛传\\番外4.txt",'a',encoding='utf-8') as f:
    f.write('番外：密嫔小传'+'\n')
url='https://www.kanunu8.com/book3/7716/169288.html'
html=getHTML(url)
parseWeb=message(html)
saveFile=txt(parseWeb)
