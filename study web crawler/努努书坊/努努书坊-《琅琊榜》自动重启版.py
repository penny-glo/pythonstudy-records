import requests
import bs4
from bs4 import BeautifulSoup
import re
import time


def getUrl(url):    #获取需爬取的网页地址(OK)
    
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='GBK'
        html1=r.text
    except:
        print('爬取失败')
    
    soup1=BeautifulSoup(html1,'html.parser')
    all_t=soup1.find_all('dd')
    bb = list()
    for i in all_t:
        try:
            title = i.string
            a = str(i.contents)
            a = a.split("\"")
            web = str(a[1])
            bb.append(web+';'+title)
        except:
            continue
    return bb
    print(bb)   #可以返回但不能打印，不知道为什么


def tryAgain(lix,n):   #每一次跳出之后从下一章开始循环
    for num in lix[n:]:
        web = str(num).split(';')
        nn = str(web[0])
        title = str(web[1])
        print(title)
        page = 'https://www.kanunu8.com/book2/11064/'+nn
        html=getHTML(page)
        if type(html) == str:
            count = n
            count = count + 1
            n = count
            parseWeb=title+'\n'+message(html)
            saveFile=txt(parseWeb)
        else:
            n = count
            tryAgain(lix,n)


def getHTML(page):  #爬取网页
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    try:
        r=requests.get(page,headers=headers,timeout=10)
        r.raise_for_status()
        r.encoding='GBK'
        return r.text
    except:
        print('不要着急，虫虫再试一次！')   #好像可以再爬一次但是好像打印不出这句话，也不知道问什么
        n = 0
        return n


def message(html):  #解析网页，获取所有小说内容(OK)
    soup=BeautifulSoup(html,'html.parser')

    all_p=soup.find_all('p')
    s = ''
    for string in all_p[1:-2]:
        s = s + str(string)

    while True:                      #用换行符替换所有的'<br/>'
        index_begin = s.find("<")
        index_end = s.find(">",index_begin + 1)
        
        if index_begin == -1:
            break
        s = s.replace(s[index_begin:index_end+1],"\n")
        
    ss = '\n' +s[1:-1]
    print(ss)
    return ss


def txt(parseWeb):  #保存为txt文件
    with open('C:\\Users\\mac\\Desktop\\琅琊榜\\琅琊榜1.txt','a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


def main():
    url='https://www.kanunu8.com/book2/11064/'
    lix = getUrl(url)
    n=0
    tryAgain(lix,n)


main()
