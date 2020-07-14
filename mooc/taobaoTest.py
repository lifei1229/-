# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
import re

findrank = re.compile(r'<td.*>(.*?)</td>', re.S)

head = {  # 模拟的头部
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    # 用户代理，告诉服务器我们是什么类型的浏览器
}

def getHTMLText(url):
    r = requests.get(url,headers = head)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def parsePage(html):
    ulist = []
    # plt = re.findall(r'view_price:[\d.]*',html)
    # tlt = re.findall(r'\"raw_title\"\:\".*？\"',html)
    plt = re.findall('"view_price":"(.*?)",', html, re.S)
    # plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
    tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
    for i in range(len(plt)):
        price = eval(plt[i].split(":")[1])
        title = eval(tlt[i].split(":")[1])
        ulist.append([price,title])
    return ulist

def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('淘宝价格', cell_overwrite_ok=True)  # 可覆盖
    col = ('商品价格', '商品名称')
    for i in range(0, 2):
        worksheet.write(0, i, col[i])  # 列名
    for i in range(len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 2):
            worksheet.write(i + 1, j, data[j])  # 数据
    workbook.save(savepath)

def main():
    goods = '书包'
    depth = 2
    path = r'./淘宝价格.xls'
    start_url = 'https://s.taobao.com/search?q=' + goods
    for i in range(depth):
        url = start_url + '&s=' + str(44*i)
        html = getHTMLText(url)
        infoList = parsePage(html)

    saveData(infoList,path)

main()