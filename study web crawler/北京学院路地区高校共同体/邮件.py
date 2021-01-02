import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText


mail_host = "smtp.163.com"
mail_sender = "gloria20210102@163.com"
mail_license = "BIJDXUZVLOOPJGVB"
mail_receivers = ["gloria20210102@163.com"]

mm = MIMEMultipart('related')

subject_content = """Python邮件测试"""
mm["From"] = "gloria20210102@163.com"
mm["To"] = "gloria20210102@163.com"
mm["Subject"] = Header(subject_content,'utf-8')

body_content = """你好，这是一个测试邮件！"""
message_text = MIMEText(body_content,"plain","utf-8")
mm.attach(message_text)

stp = smtplib.SMTP()
stp.connect(mail_host, 25)  
stp.set_debuglevel(1)
stp.login('gloria20210102@163.com','BIJDXUZVLOOPJGVB')
stp.sendmail("gloria20210102@163.com", "gloria20210102@163.com", mm.as_string())
print("邮件发送成功")
stp.quit()
