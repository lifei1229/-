# -*- coding=utf-8 -*-
import requests
import os
path = r'./'
url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
root = r'./imgs/'
if not os.path.exists(root):
    os.mkdir(root)
path = root + url.split('/')[-1]
r = requests.get(url)
with open(path,'wb') as f:
    f.write(r.content)
