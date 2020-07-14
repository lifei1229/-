# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'http://python123.io/ws/demo.html'
r = requests.get(url)
r = r.text
soup = BeautifulSoup(r,"html.parser")
# print(soup.prettify())
print(soup.find_all(['a','b']))
