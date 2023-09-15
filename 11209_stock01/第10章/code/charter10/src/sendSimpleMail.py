# !/usr/bin/env python
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
# 群組織信件        
message = MIMEText('Python 信件傳送測試', 'plain', 'utf-8')
message['Subject'] = 'Hello,用Python傳送信件'
sendMail('hsm_computer','xxx','hsm_computer@163.com','hsm_computer@163.com',message.as_string())    