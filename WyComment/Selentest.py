# -*- coding=utf-8 -*-
from selenium import webdriver
import time
driver = webdriver.Chrome(executable_path='chromedriver.exe')    # Chrome浏览器
driver.get("https://www.baidu.cn")