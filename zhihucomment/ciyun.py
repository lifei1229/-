import wordcloud
import matplotlib.pyplot as plt
import requests
import json
import jieba
import binascii
from urllib.parse import urlencode
import sys

f = open('outputs.txt', 'r', encoding='utf-8')
txt = f.read()
w = wordcloud.WordCloud(width=1000,
                        height=700,
                        background_color='white',
                        font_path='msyh.ttc')
w.generate(txt)
w.to_file('outputs.png')