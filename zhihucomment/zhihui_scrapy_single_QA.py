import requests
from bs4 import BeautifulSoup
import json
import re
REG = re.compile('<[^>]*>')

id = '401037012'

def extract_answer(s):
    temp_list = REG.sub("", s).replace("\n", "").replace(" ","")
    return temp_list


headers = {
        'origin': 'https://www.zhihu.com',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '_xsrf=ZZSqtWI3hrOsG93lCyXvecWde5amydDP; _zap=252a8de0-4adf-47c1-9dab-8114d04f0747; d_c0="AADu7ByLdRCPTpNAK4uo8jhzpXFV1gVDFBQ=|1575546111"; __utma=51854390.1222330378.1580614776.1580614776.1580614776.1; __utmz=51854390.1580614776.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E7%9F%A5%E4%B9%8E%20; __utmv=51854390.000--|3=entry_date=20200202=1; z_c0=Mi4xNl9SOENRQUFBQUFBQU83c0hJdDFFQmNBQUFCaEFsVk5wR2d5WHdBR0ZmaGNoSXNpWVMyMXVobVNFQTlzS3Fyc0Z3|1581587108|f8a3574a7e06fd9983c76e819c274d8e39f00c88; _ga=GA1.2.1222330378.1580614776; q_c1=e1df34001aec476d8dfae2c376a11fcc|1589456443000|1580614776000; _gid=GA1.2.382318960.1590891599; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1590976710,1590976764,1590977162,1590977331; tst=r; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1590978039; KLBRSID=5430ad6ccb1a51f38ac194049bce5dfe|1590978044|1590975667; _gat_gtag_UA_149949619_1=1',
        'referer': 'https://www.zhihu.com/question/'+id,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'
}

start_url = 'https://www.zhihu.com/api/v4/questions/'+ id + '/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit=5&offset=0&sort_by=default'

print("running.")

next_url = [start_url]
count = 0

for url in next_url:
    html = requests.get(url, headers=headers)
    html.encoding = html.apparent_encoding
    soup = BeautifulSoup(html.text, "lxml")
    content = str(soup.p).split("<p>")[1].split("</p>")[0]
    c = json.loads(content)

    if "data" not in c:
        print("获取数据失败，本 ip 可能已被限制。")
        print(c)
        break

    answers = [extract_answer(item["content"]) for item in c["data"] if extract_answer(item["content"]) != ""]

    with open(id+'.txt', 'a', encoding='utf-8') as f:
        for answer in answers:
            f.write(answer + '\n')
            f.write('\n')
            count = count + 1
            print("answer", count)

    next_url.append(c["paging"]["next"])
    if c["paging"]["is_end"]:
        break

print("total answers:",count)