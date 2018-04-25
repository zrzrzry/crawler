import scrapy
import re
import json
from scrapy.http import Request
# from Spider.items import ArticleItem
from Spider.items import ServantItem

class fgo_wiki_servant(scrapy.Spider):
    name = 'fgo_wiki_servant'
    #allowed_domains = ['.com']
    start_urls = ['https://fgowiki.com/guide']

    def parse(self, response):
        #分析fgowiki的页面结构发送请求获取动态页面的数据
        post_url='https://api.umowang.com/guides/data/fgo?jsoncallback=getguidedata&command=pets_list_all&page=4&params='
        #post_url='https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv337&productId=3311073&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0'
        yield Request(url=post_url, callback=self.parse_detail)
        print(post_url)
    pass

    def parse_detail(self, response):
        #获取servant具体数据
        servant = ServantItem()
        
    pass