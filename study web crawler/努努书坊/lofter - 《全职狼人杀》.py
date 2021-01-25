import requests
import bs4
from bs4 import BeautifulSoup
import re
import time


def getUrl(url):    #获取需爬取的网页地址
    
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding='UTF8'
        html1=r.text
    except:
        print('爬取失败')
    
    soup1=BeautifulSoup(html1,'html.parser')
    all_t=soup1.find_all('a',target="_blank")
    bb = list()
    for t in all_t[:-2]:
        try:
            web = t['href']
            bb.append(web)
        except:
            continue
    return bb
    print(bb)   #可以返回但不能打印，不知道为什么


def tryAgain(lix,n):   #每一次跳出之后从下一章开始循环
    for num in lix[n:]:
        page = num
        html=getHTML(page)
        if type(html) == str:
            count = n
            count = count + 1
            n = count
            parseWeb='chapter '+str(n)+'\n'+message(html)
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
        r.encoding='UTF8'
        return r.text
    except:
        print('不要着急，虫虫再试一次！')   #好像可以再爬一次但是好像打印不出这句话，也不知道问什么
        n = 0
        return n


def message(html):  #解析网页，获取所有小说内容(OK)
    soup=BeautifulSoup(html,'html.parser')

    all_p=soup.find_all('p')
    s = ''
    for string in all_p[1:-1]:
        s = s + '\n' + string.text
        
    ss = '\n' +s
    print(ss)
    return ss


def txt(parseWeb):  #保存为txt文件
    with open('C:\\Users\\mac\\Desktop\\狼人杀\\狼人杀.txt','a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


def main():
    url='https://fanyingman.lofter.com/post/1d87737e_124d641b'
    lix = getUrl(url)
    n=0
    tryAgain(lix,n)


main()

