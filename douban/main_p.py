import requests

url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

page = requests.get(url).content.decode('utf-8')

import re

#reg = '<script id="getListByCountryTypeService2">([^<]+)'
reg = '<script id="getListByCountryTypeService1">([^<]+)'
data = re.findall(reg, page)[0][43:-11]

import  json

data = json.loads(data)

import pandas as pd
from datetime import  datetime

for row in data:
    for key in row:
        if key in ['createTime','modifyTime']:
            row[key] = datetime.fromtimestamp(row[key]/1000).strftime('%Y-%m-%d %H:%M:%S')


df = pd.DataFrame(data)

df.to_csv('最新肺炎数据2.csv', mode='a')


