# -*- coding=utf-8 -*-
import requests
url = 'http://www.baidu.com/s'
keyword = 'Python'
kv = {'wd':keyword}
r = requests.get(url, params=kv)
print(r.request.url)
# print(r.text)