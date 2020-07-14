# -*- coding:UTF-8 -*-
import requests
import sys
import re
import urllib.request
import urllib.error
import xlwt
from bs4 import BeautifulSoup
import sqlite3


def main():
    baseurl = 'https://movie.douban.com/top250?start='
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = './豆瓣Top250m.xls'
    saveData2(datalist, savepath)


findlink = re.compile(r'<a href="(.*?)">')  # 创建正则表达对象，表示规则
findname = re.compile(r'<span class="title">(.*)</span>')  # 创建正则表达对象，表示规则
findImg = re.compile(r'<img.*src="(.*?)"', re.S)  # 让换行符在在字符串中
findSore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)
findtime = re.compile(r'<p class="">(.*?)</p>', re.S)
findnum = re.compile(r'<br/>(\d*.*/.*)/.*')
# 爬取网页


def getData(baseurl):
    datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 25)  # 获取所有的网页
        html = askURL(url)

        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # 查找符合要求的字符串，形成列表
        for item in soup.find_all('div', class_="item"):  # div 同时是class属性，加下划线
            # print(item) #查看电影item
            data = []
            item = str(item)
            link = re.findall(findlink, item)[0]
            data.append(link)
            img = re.findall(findImg, item)[0]
            data.append(img)
            name = re.findall(findname, item)  # 可能只有一个名字
            if len(name) == 2:
                oname = name[1].replace("/", "")  # 添加国外的名字
                data.append(name[0])
                data.append(oname)
            else:
                data.append(name)
                data.append('')
            score = re.findall(findSore, item)[0]
            data.append(score)
            judge = re.findall(findJudge, item)[0]
            data.append(judge)
            bd = re.findall(findBd, item)[0]
            bd = re.sub(r'<br(\s+)?/>(\s+)', ' ', bd)  # 去掉<br/>
            bd = re.sub('/', ' ', bd)
            data.append(bd.strip())  # 去掉空格

            title = re.findall(findtime, item)[0].strip()
            t1 = "".join(title.split())
            # print(t1)
            times = re.findall(findnum, t1)[0]
            data.append(times)

            datalist.append(data)
    # print(datalist)
    return datalist

# 得到指定一个url的网页内容


def askURL(url):
    head = {  # 模拟的头部
        "User-Agent": " Mozilla/5.0(Windows NT 10.0;WOW64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/78.0.3904.108Safari/537.36"
        # 用户代理，告诉服务器我们是什么类型的浏览器
    }
    request = urllib.request.Request(url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(request)  # response便是网页信息
        html = response.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 3.保存数据
def saveData(datalist, savepath):

    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 可覆盖
    col = ('电影链接', '图片链接', '影片中文名', '影片外国名', '评分', '评价数', '影片信息')
    for i in range(0, 7):
        worksheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 7):
            worksheet.write(i + 1, j, data[j])  # 数据
    workbook.save(savepath)


def saveData2(datalist, savepath):

    workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
    worksheet = workbook.add_sheet('豆瓣电影Top250', cell_overwrite_ok=True)  # 可覆盖
    col = ('影片中文名', '评分', '评价数', '时间/地区')
    for i in range(0, 4):
        worksheet.write(0, i, col[i])  # 列名
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        worksheet.write(i + 1, 0, data[2])  # 影片中文名
        worksheet.write(i + 1, 1, data[4])  # 评分
        worksheet.write(i + 1, 2, data[5])  # 评价数
        worksheet.write(i + 1, 3, data[7])  # 时间/地区
    workbook.save(savepath)


if __name__ == '__main__':  # 程序执行的时候，运行下面的程序(程序的入口)
    main()
    print("done!")
