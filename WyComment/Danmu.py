# -*- coding=utf-8 -*-
from selenium import webdriver
# import time
# driver = webdriver.Chrome(executable_path='chromedriver.exe')    # Chrome浏览器
# driver.get("https://www.baidu.cn")

from selenium.webdriver.chrome.options import Options



class YunSpider(object):
    #初始化
    def __init__(self,url):
        self.url = url
        self.driver = webdriver.Chrome(executable_path='chromedriver.exe')

#打开网站，实例方法
    def getContent(self):
        self.driver.get(self.url)
        # js = 'window.scrollBy(0,8000)'
        # self.driver.execute_script(js)
        self.driver.implicitly_wait(10)
        # //任意节点 .//从上个节点开始 /下面一个节点
        selectors = self.driver.find_elements_by_xpath('//div[@class="list-item reply-wrap "]/div')
        for selector in selectors:
            text = selector.find_element_by_xpath('.//*[@id="comment"]/div/div[2]/div[1]/div[4]/div[1]/div[2]/p').text
            # text = selector.get_attribute('title')
            print(text)
            # self.saveData(text)
            YunSpider.saveData(text)


    @staticmethod
    def saveData(item):
        with open('danmu.txt','a',encoding='utf-8') as f:
            f.write(item + '\n')
            f.write('*'*20 + '\n')

if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/BV12x411f7fe/?spm_id_from=trigger_reload'
    yunspder = YunSpider(url)
    yunspder.getContent()