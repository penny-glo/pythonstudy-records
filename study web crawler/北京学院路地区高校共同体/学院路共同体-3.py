'''
1.4 修订初期完成版
本来试图每天自动启动进行爬取然后将其发送到邮箱中的，但Windows系统一直不关机也不现实，也没有找到很好的方法能每天自动启动爬取，最后只能取消这一设想，改为每天打开该程序人工查看到底改了没有
发邮件的功能也因此变的很鸡肋
不过这应该是很长一段时间我的完成版，不知道之后能不能找到更好的解决方法，比如……学一个linux系统（头秃）
这是我琢磨几天完成的第一个爬虫，还是要纪念一下！
'''

import requests
import bs4
from bs4 import BeautifulSoup
import re
import time
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText

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
        print(history[-3:])

        if now[-3:] == '358':
            print('未发现更新！')
        else:
            print('发现更新!')
            sendEmail('发现更新！'+now[-3:])
            tmp [history] = now
    else:
        tmp['history'] = parseWeb
        history = tmp['history']
        print('first time')
        print(history[-3:])

def sendEmail(text):
    mail_host = "smtp.163.com"
    mail_sender = "gloria20210102@163.com"
    mail_license = "BIJDXUZVLOOPJGVB"
    mail_receivers = ["gloria20210102@163.com"]

    mm = MIMEMultipart('related')

    subject_content = """北京学院路地区高校共同体更新"""
    mm["From"] = "gloria20210102@163.com"
    mm["To"] = "gloria20210102@163.com"
    mm["Subject"] = Header(subject_content,'utf-8')

    body_content = text
    message_text = MIMEText(body_content,"plain","utf-8")
    mm.attach(message_text)

    stp = smtplib.SMTP()
    stp.connect(mail_host, 25)  
    stp.set_debuglevel(1)
    stp.login('gloria20210102@163.com','BIJDXUZVLOOPJGVB')
    stp.sendmail("gloria20210102@163.com", "gloria20210102@163.com", mm.as_string())
    print("邮件发送成功")
    stp.quit()

tmp = {'history':None}
while True:
    uinfo = []
    url="http://www.xueyuanlu.cn/article/index.php?category_id=3"
    html = getHTML(url)
    parseWeb=message(html)
    check()
    time.sleep(60)
    print('\n继续工作！')
