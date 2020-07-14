# -*- coding=utf-8 -*-
from selenium import webdriver
import time
# driver = webdriver.Chrome(executable_path='chromedriver.exe')    # Chrome浏览器
# driver.get("https://www.baidu.cn")

class YunSpider(object):
    #初始化
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

#打开网站，实例方法
    def getContent(self):
        self.driver.get(self.url)
        #进入内嵌网页
        self.driver.switch_to.frame(0) #0代表是第一个框
        js = 'window.scrollBy(0,8000)'
        self.driver.execute_script(js)
        #翻页
        for page in range(2):
            # //任意节点 .//从上个节点开始 /下面一个节点
            selectors = self.driver.find_elements_by_xpath('//div[@class="cmmts j-flag"]/div')
            for selector in selectors:
                text = selector.find_element_by_xpath('.//div[@class="cnt f-brk"]').text
                # print(text)
                # self.saveData(text)
                YunSpider.saveData(text)

            #找到下一页的元素点击
            # find_element_by_partial_link_text 获取文本链接，模糊匹配
            nextPage = self.driver.find_element_by_partial_link_text('下一页')
            # 点击下一页
            nextPage.click()
            time.sleep(0.5)

    @staticmethod
    def saveData(item):
        with open('yun.txt','a',encoding='utf-8') as f:
            f.write(item + '\n')
            f.write('*'*20 + '\n')

if __name__ == '__main__':
    url = 'https://music.163.com/#/song?id=417250673'
    yunspder = YunSpider(url)
    yunspder.getContent()