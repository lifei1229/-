# -*- encoding: utf-8 -*-
import requests
import re
import os
from bs4 import BeautifulSoup

findImg = re.compile(r'<img src="(.*?)"', re.S)  # 让换行符在在字符串中
#  定义下载图片的方法
def downloadPic(url, path):
    i = 0  # 使用global声明这是一个全局变量,方法内无法直接使用全局变量
    html = requests.get(url).text
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)

    for each in pic_url:
        print("正在下载第" + str(i) + "张图片,图片地址:" + each)

        try:
            # 可能有些图片存在网址打不开的情况,这里设置一个5秒的超时控制
            pic = requests.get(each, timeout=5)
        except Exception:  # 出现异常直接跳过
            print("【错误】当前图片无法下载")
            continue  # 跳过本次循环

        #  定义变量保存图片的路径
        string = path + "/" + str(i) + ".jpg"
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':  # 主程序
    name = input("请输入您想要下载的图片:")

    #  先根据搜索的关键字判断存放该类别的文件夹是否存在,不存在则创建
    path = r"C:/spyder/baiduImg/imges/" + name

    if not os.path.exists(path):
        os.mkdir(path)

    #  根据输入的内容构建url列表推导式，百度图片搜索每页20张图片
    urls = [
        'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' +
        name +
        '&ct=201326592&v=flip&pn={}'.format(
            str(i)) for i in range(
            0,
            100,
            20)]
    for url in urls:
        downloadPic(url, path)

    print("下载完成!")
