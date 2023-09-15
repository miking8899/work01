# !/usr/bin/env python
# coding=utf-8
from wsgiref.simple_server import make_server
def myWebApp(environ, response):
    response('200 OK', [('Content-Type', 'text/html')])
    return ['Web Page Created by WSGI.'.encode(encoding='utf_8')]

# 建立一個伺服器，通訊埠是8080，用於處理的方法是myWebApp
httpd = make_server('localhost', 8080, myWebApp)
print("Starting HTTP Server on 8080...")
# 監聽HTTP請求，若果有請求，則呼叫myWebApp方法進行處理
httpd.serve_forever()