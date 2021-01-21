import requests
import bs4
from bs4 import BeautifulSoup
import re
import time

def getUrl(url):    #获取需爬取的网页地址
    html1=getHTML(url)
    soup1=BeautifulSoup(html1,'html.parser')
    all_a=soup1.find_all('a',href=re.compile("\d\d\d\d\d.html"))
    bb = list()
    for aa in all_a:
        bb.append(aa['href'])
    print(bb)
    return bb
    

def getHTML(page):  #爬取网页
    try:
        r=requests.get(page)
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
    with open("C:\\Users\\mac\\Desktop\\后宫·甄嬛传\\4.txt",'a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


#主程序
url='https://www.kanunu8.com/book/3816/'    #需修改
lix = getUrl(url)

with open("C:\\Users\\mac\\Desktop\\后宫·甄嬛传\\4.txt",'a',encoding='utf-8') as f:
    f.write('后宫·甄嬛传4'+'\n')
    
    
for num in lix:
    page = 'https://www.kanunu8.com/book/3816/'+num #需修改
    html=getHTML(page)
    parseWeb=message(html)
    saveFile=txt(parseWeb)
    time.sleep(5)
