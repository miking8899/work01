﻿# !/usr/bin/env python
# coding=utf-8
import smtplib
from email.mime.text import MIMEText
# 傳送信件
def sendMail(username,pwd,from_addr,to_addr,msg):
    try:
        smtp = smtplib.SMTP() 
        smtp.connect('smtp.163.com') 
        smtp.login(username, pwd) 
        smtp.sendmail(from_addr,to_addr, msg) 
        smtp.quit()
    except Exception as e:  
        print(str(e))
HTMLContent = '<html><head></head><body>'\
 '<h1>Hello</h1>This is <a href="https://www.cnblogs.com/JavaArchitect/">My Blog.</a>'\
 '</body></html>'        
message = MIMEText(HTMLContent, 'html', 'utf-8')
message['Subject'] = 'Hello,用Python傳送信件'
message['From'] = 'hsm_computer'        # 信件上顯示的發件人
message['To'] = 'hsm_computer@163.com'  # 信件上顯示的收件人
sendMail('hsm_computer','xxx','hsm_computer@163.com','hsm_computer@163.com',message.as_string())    