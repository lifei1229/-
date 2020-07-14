import wordcloud
import matplotlib.pyplot as plt
import requests
import json
import jieba
import binascii
from urllib.parse import urlencode
import sys


def get_json(url):

    headers = {

        'cookie' : '_xsrf=ZZSqtWI3hrOsG93lCyXvecWde5amydDP; _zap=252a8de0-4adf-47c1-9dab-8114d04f0747; d_c0="AADu7ByLdRCPTpNAK4uo8jhzpXFV1gVDFBQ=|1575546111"; __utma=51854390.1222330378.1580614776.1580614776.1580614776.1; __utmz=51854390.1580614776.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%9F%A5%E4%B9%8E%20; __utmv=51854390.000--|3=entry_date=20200202=1; z_c0=Mi4xNl9SOENRQUFBQUFBQU83c0hJdDFFQmNBQUFCaEFsVk5wR2d5WHdBR0ZmaGNoSXNpWVMyMXVobVNFQTlzS3Fyc0Z3|1581587108|f8a3574a7e06fd9983c76e819c274d8e39f00c88; _ga=GA1.2.1222330378.1580614776; q_c1=e1df34001aec476d8dfae2c376a11fcc|1589456443000|1580614776000; _gid=GA1.2.382318960.1590891599; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590976710,1590976764,1590977162,1590977331; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590978039; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1590978044|1590975667; _gat_gtag_UA_149949619_1=1',
       
        'referer': 'https://www.zhihu.com/question/401037012',

        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

    }

    response = requests.get(url, headers=headers)

    response.encoding = response.apparent_encoding

    return response.content


def get_comments(code_json):
    json_dict = json.loads(code_json.decode('utf-8'))
    for item in json_dict['data']:
        # 16进制转化为字符串
        comment = item['content'].encode('utf-8')
        comment = binascii.b2a_hex(comment)
        comment = binascii.a2b_hex(comment).decode("utf8")
        yield comment

def wordcloud_(all_comments):
    # 对句子进行分词，加载停用词
    # 打开和保存文件时记得加encoding='utf-8'编码，不然会报错。
    def seg_sentence(sentence):
        sentence_seged = jieba.cut(sentence.strip(), cut_all=False)  # 精确模式
        stopwords = [line.strip() for line in open('stopwords.txt', 'r', encoding='utf-8').readlines()]  # 这里加载停用词的路径
        outstr = ''
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr

    for line in all_comments:
        line_seg = seg_sentence(line)  # 这里的返回值是字符串
        with open('wzry.txt', 'a', encoding='utf-8') as f:
            f.write(line_seg + '\n')

    f = open('wzry.txt', 'r', encoding='utf-8')
    txt = f.read()
    w = wordcloud.WordCloud(width=1000,
                            height=700,
                            background_color='white',
                            font_path='msyh.ttc')
    w.generate(txt)
    w.to_file('wzry.png')


def main():
    comment_list = []
    for i in range(0,800,20):
        url = "https://www.zhihu.com/api/v4/answers/401037012/root_comments?"
        data = {
            'include': 'data[*].author,collapsed,reply_to_author,disliked,content,voting,vote_count,is_parent_author,is_author',
            'order': 'normal',
            'limit': '20',
            'offset': i,
            'status': 'open'
        }
        data = urlencode(data)
        url = url + data
        code_json = get_json(url)
        sys.stdout.write("  已下载:%.3f%%" %  float(i/800*100) + '\r')#不能同时两行刷新
        sys.stdout.flush()
        for reslut in get_comments(code_json):
            #print(reslut)
            comment_list.append(reslut)
    wordcloud_(comment_list)

if __name__ == '__main__':
    main()