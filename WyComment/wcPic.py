# -*- coding=utf-8 -*-


import wordcloud
import jieba

# # 构建词云对象w，设置词云图片宽、高、字体、背景颜色等参数
# w = wordcloud.WordCloud(width=1000,
#                         height=700,
#                         background_color='white',
#                         font_path='msyh.ttc')
#
# w.generate('从明天起，做一个幸福的人。喂马、劈柴，周游世界。从明天起，关心粮食和蔬菜。我有一所房子，面朝大海，春暖花开')
#
# w.to_file('output2-poem.png')

word_frequency = dict()

# module_path = os.path.abspath(os.curdir)

f = open('stopWordList.txt', encoding='utf-8')
txt = f.read()

words = jieba.cut(txt)
# 统计词频
for word in words:
    if word not in word_frequency:
        word_frequency[word] = 1
    else:
        word_frequency[word] += 1

print(word_frequency)