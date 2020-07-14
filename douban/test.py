# -*- coding:UTF-8 -*-

import urllib.request,urllib.error

#获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))

# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'hello':"wordl"}),encoding='utf-8') #用户名密码或者cookie
# response = urllib.request.urlopen("http://httpbin.org/post",data=data) #用data来封装
# print(response.read().decode('utf-8'))

#get请求，不需要传递信息
# 超时处理,是必要的
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
#     #区别就是 代理不一样，"User-Agent": "Python-urllib/3.5", 明显是爬虫的
# except urllib.error.URLError as e:
#     print("time out!")

# #
# response = urllib.request.urlopen("http://www.baidu.com",timeout=1)
# print(response.status) #状态码，404；418被发现查重
# # print(response.getheaders())
# print(response.getheader('Set-Cookie'))

'''
# 418了怎么办
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
url = 'http://httpbin.org/post'
data = bytes(urllib.parse.urlencode({'name':"eric"}),encoding='utf-8')
req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
#headers表示要返回哪些信息
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
'''

#访问豆瓣
url = 'https://movie.douban.com/top250?start=50'
headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
}
# data = bytes(urllib.parse.urlencode({'name':"eric"}),encoding='utf-8')
req = urllib.request.Request(url=url,headers=headers)
#headers表示要返回哪些信息
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))