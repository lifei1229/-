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
file = open("baidu.html",'rb')
html = file.read()
bs = BeautifulSoup(html,"html.parser") #定义一个对象
# print(bs.title) #从头开始往下找
# print(bs.title.string)
# print(bs.a)
# print(bs.head)  #默认找到第一个标签及其内容
# print(bs.a.attrs) #用字典获得内容
# print(bs) #表示整个文档 树形结构

# print(bs.a)

#-------------------------------------
#文档遍历
# print(bs.head.contents) #得到列表
# print(bs.head.contents[0])
#文档搜索
#字符串过滤
# t_list = bs.find_all('a') #找到所有a标签

#正则表达式搜索，使用search()
# t_list = bs.find_all(re.compile('a')) #所有包含a字符都会被显示出来

# #用函数来搜索 不常用
# def name_is_exists(tag):
#     return tag.has_attr('name')
# t_list = bs.find_all(name_is_exists)

# print(t_list)

#2 kwargs 参数
# t_list = bs.find_all(id='head')
# t_list = bs.find_all(herf="http://news.baidu.com")
# t_list = bs.find_all(text=re.compile("\d"))
# for item in t_list:
#     print(item)


# text文本
# t_list = bs.find_all(text=['百度一下','贴吧'])
# print(t_list)

# css 选择器 可以通过标签查找，id，类名等
# print(bs.select('title'))
# print(bs.select('a[class="bri"]')) #通过属性查找
# print(bs.select('head > title')) #通过子标签查找
t_list= bs.select(".mav ~. bri")
print(t_list[0].get_text())
