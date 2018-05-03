import scrapy
import re
import json
from scrapy.http import Request
from Spider.items import ServantItem
from selenium import webdriver
import time

class fgo_wiki_servant(scrapy.Spider):
    name = 'fgo_wiki_servant'
    #allowed_domains = ['.com']
    start_urls = ['https://fgowiki.com/guide']


    def parse(self, response):
        #分析fgowiki的页面结构发送请求获取动态页面的数据
        #使用selenium实现scrapy对浏览器的调用
        # 调用浏览器加载动态页面
        browser = webdriver.Chrome()
        browser.get(response.url)
        # 将页面滚动条拖到底部
        count = 1
        n = 20
        while count < n :
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(0.1)
            count += 1
        #休息一下等页面加载完。。。
        time.sleep(5)

        servant_nums = browser.find_elements_by_class_name('pull-left').__len__()
        # 提取出从者详细信息页面的url
        temp = 1
        while temp < 2:
            url_count = str(temp)
            servant_id = temp
            servant_url = browser.find_element_by_css_selector('[data-id="' + url_count + '"] a').get_attribute("href")
            servant_avatar_url = browser.find_element_by_css_selector('[data-id="' + url_count + '"] .td.img.fl img').get_attribute("src")
            print(servant_url)
            print(servant_avatar_url)
            yield Request(url=servant_url, callback=self.parse_detail(id=servant_id), meta={"servant_avatar_url":servant_avatar_url})
            temp += 1
        #关闭浏览器
        browser.close()
    pass

    def parse_detail(self, response, id):
        #获取servant具体数据
        browser = webdriver.Chrome()
        browser.get(response.url)
        #response.xpath('//*[@id="row-move"]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[1]/th/div')
        #爬取关键数据
        servant_name = browser.find_element_by_css_selector('.NAME').text
        servant_name_en = browser.find_element_by_css_selector('.NAME_EN').text
        servant_name_jp = browser.find_element_by_css_selector('.NAME_JP').text
        servant_class = browser.find_element_by_css_selector('.')

        servant = ServantItem()
        servant['name'] = servant_name
        servant['id'] = id

    pass