# -*- coding:UTF-8 -*-
import requests
import sys
import re
import urllib.request,urllib.error
import xlwt
from bs4 import BeautifulSoup

'''
-Tag 标签及其内容
-NavigableString 标签里面的内容，字符串
-BeautifulSoup 自身类型 文档
-Comment  特殊的navigableString
'''
file = open(r"C:/极客时间/爬虫/1.html",'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser") #定义一个对象
bs = str(bs)
# print(bs)
time = re.compile(r'<p class="">(.*?)</p>',re.S)
title = re.findall(time, bs)[0].strip()
t1 = "".join(title.split())
print(t1)
num = re.compile(r'<br/>(\d*/.*)/.*')
# title =re.sub("\D", "", title)
title = re.findall(num, t1)[0]
print(title)