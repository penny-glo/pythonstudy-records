import requests
import bs4
from bs4 import BeautifulSoup
import re
import time

def getHTML(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return '404'

def message(html):
    soup=BeautifulSoup(html,'html.parser')
    for link in soup.find_all('a',href=re.compile("view"),string=re.compile('通知'),limit=1):
        info_link=link.get('href')
        info_text=link.get_text(strip=True)
        print(info_text)
    return info_link


def check():
    if (tmp['history']):
        history = tmp['history']
        now = parseWeb

        if history[-3:0] == now[-3:0]:
            result = ''
            print('未发现更新！')
        else:
            print('发现更新')
            
            tmp [history] = now
    else:
        tmp['history'] = parseWeb
        print('first time')


tmp = {'history':None}
while True:
    uinfo = []
    url="http://www.xueyuanlu.cn/article/index.php?category_id=3"
    html = getHTML(url)
    parseWeb=message(html)
    check()
    print('\n休息5秒继续运行！')
    time.sleep(5)
    print('继续工作！')
