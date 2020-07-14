# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import bs4
import xlwt
import re

findrank = re.compile(r'<td.*>(.*?)</td>', re.S)


def getHTMLText(url):
    r = requests.get(url,timeout=30)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    return r.text

def fillUnivList(html):
    ulist = []
    soup = BeautifulSoup(html,'html.parser')
    # for tr in soup.find('tbody').children:
    #     if isinstance(tr,bs4.element.Tag):
    #         tds = tr('td')
    #         ulist.append([tds[0].string,tds[1].string,tds[3].string])
    for item in soup.find_all('tr')[1:]:
        rank = item.find_all('td')[0].string
        name = item.find_all('td')[1].string
        score = item.find_all('td')[3].string
        ulist.append([rank,name,score])
    return ulist

def saveData(datalist, savepath):
    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('大学排名', cell_overwrite_ok=True)  # 可覆盖
    col = ('排名', '学校名称', '总分')
    for i in range(0, 3):
        worksheet.write(0, i, col[i])  # 列名
    for i in range(len(datalist)):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 3):
            worksheet.write(i + 1, j, data[j])  # 数据
    workbook.save(savepath)

if __name__ == '__main__':
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    path = r'./大学排名.xls'
    html = getHTMLText(url)
    uinfo = fillUnivList(html)
    saveData(uinfo,path)

