'''
之前看txt就觉得《暗恋·橘生淮南》看着不舒服，自己得空重新爬了一个
这一版倒可以输出'不要着急，虫虫再试一次'了，不过一般来讲重爬三次会自动退出
虫虫好可爱！
'''

import requests
import bs4
from bs4 import BeautifulSoup
import re
import time


def tryAgain(lix,n):   #每一次跳出之后从下一章开始循环
    for num in lix[n:]:
        nn = str(num)
        page = 'https://www.890h.com'+nn
        html=getHTML(page)
        if type(html) == str:
            count = n
            count = count + 1
            n = count
            parseWeb = message(html)
            saveFile = txt(parseWeb)
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


def message(html):  #解析网页，获取所有小说内容
    soup=BeautifulSoup(html,'html.parser')
    h = soup.find('h1')
    title = h.string
    print(title)
    d = soup.find_all('div',id = 'content')
    s = ''
    for string in d:
        s = s + str(string)

    while True:                      #用换行符替换所有的'<br/>'
        index_begin = s.find("<")
        index_end = s.find(">",index_begin + 1)
        
        if index_begin == -1:
            break
        s = s.replace(s[index_begin:index_end+1],"\n")
        
    ss = title + '\n' +s
    print(ss)
    return ss


def txt(parseWeb):  #保存为txt文件
    with open('C:\\Users\\mac\\Desktop\\暗恋·橘生淮南\\暗恋·橘生淮南-测试.txt','a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


def main():
    url='https://www.kanunu8.com/book2/11064/'
    lix = ["/26_26135/18051627.html","/26_26135/18051628.html"]
    with open('C:\\Users\\mac\\Desktop\\暗恋·橘生淮南\\暗恋·橘生淮南.txt','a',encoding='utf-8') as f:
        f.write('暗恋·橘生淮南'+ '\n')
    n=0
    tryAgain(lix,n)


main()
