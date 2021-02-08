import requests
import bs4
from bs4 import BeautifulSoup
import re
import time



def tryAgain(n):   #每一次跳出之后从下一章开始循环
    for num in range(n,6):
        page = 'https://tieba.baidu.com/p/2553585140?see_lz=1&pn='+str(n)
        html=getHTML(page)
        if type(html) == str:
            count = n
            count = count + 1
            n = count
            parseWeb=message(html)
            saveFile=txt(parseWeb)
        else:
            n = count
            tryAgain(n)


def getHTML(page):  #爬取网页
    headers={
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
    }
    try:
        r=requests.get(page,headers=headers,timeout=10)
        r.raise_for_status()
        r.encoding='utf-8'
        return r.text
    except:
        print('不要着急，虫虫再试一次！')   #好像可以再爬一次但是好像打印不出这句话，也不知道问什么
        n = 0
        return n


def message(html):  #解析网页，获取所有小说内容(OK)
    soup=BeautifulSoup(html,'html.parser')

    all_p=soup.find_all('cc')
    s = ''
    for string in all_p[2:-2]:
        s = s + string.text
    ss = '\n' +s
    print(ss)
    return ss


def txt(parseWeb):  #保存为txt文件
    with open('C:\\Users\\mac\\Desktop\\百度贴吧\\【耽美】梦入华年.txt','a',encoding='utf-8') as f:
        f.write(parseWeb + '\n')


def main():
    n=1
    tryAgain(n)


main()
