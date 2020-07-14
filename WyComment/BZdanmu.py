# -*- coding=utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import jieba
import wordcloud

# 根据av号获取cid


def cid_from_av(av):
    url = 'http://www.bilibili.com/video/bv' + str(av)
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text

    # 用try防止有些av号没视频
    try:
        soup = BeautifulSoup(html, 'lxml')
        # 视频名
        title = soup.select('meta[name="title"]')[0]['content']
        # 投稿人
        author = soup.select('meta[name="author"]')[0]['content']
        # 弹幕的网站代码
        danmu_id = re.findall(r'cid=(\d+)&', html)[0]
        #print(title, author)
        return {
            'status': 'ok',
            'title': title,
            'author': author,
            'cid': danmu_id}
    except BaseException:
        print('视频不见了!')
    return {'status': 'no'}


# 获取弹幕
def get_danmu(cid,fileName):
    url = 'http://comment.bilibili.com/' + str(cid) + '.xml'
    req = requests.get(url)
    html = req.content
    html_doc = str(html, 'utf-8')  # 修改成utf-8

    # 解析
    soup = BeautifulSoup(html_doc, "lxml")
    results = soup.find_all('d')
    contents = [x.text for x in results]
    # print(contents)
    saveData(contents,fileName)
    return contents


def saveData(items, fileName):
    with open(fileName, 'a', encoding='utf-8') as f:
        for item in items:
            f.write(item + '\n')

# 弹幕分词


def danmu_cut(fileName):
    word_frequency = dict()
    # 获取停止词
    stop_word = []

    f = open(fileName, encoding='utf-8')
    txt = f.read()
    # 分词
    words = jieba.cut(txt)
    # 统计词频
    for word in words:
        if word not in stop_word:
            word_frequency[word] = word_frequency.get(word, 0) + 1
    return word_frequency


def dro_wc(cid,fileName):
    f = open(fileName, encoding='utf-8')
    txt = f.read()
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='msyh.ttc')
    w.generate(txt)
    w.to_file(str(cid) + '.png')


if __name__ == '__main__':
    bv = '1Xt411C7qJ'
    fileName = bv + '.txt'
    avInfo = cid_from_av(bv)
    cid = avInfo['cid']
    danmus = get_danmu(cid,fileName)
    # word_frequency = danmu_cut(fileName)
    wordFile = dro_wc(bv,fileName)
