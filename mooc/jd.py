# -*- coding=utf-8 -*-
import requests


head = {  # 模拟的头部
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 用户代理，告诉服务器我们是什么类型的浏览器
}
# url = 'https://item.jd.com/2967929.html'
url2 = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
r = requests.get(url2, headers=head)
r.raise_for_status()
r.encoding = r.apparent_encoding
print(r.text[1:1000])



