# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/113854/']

    def parse(self, response):
        title = response.xpath('//*[@class="entry-header"]/h1/text()')
        create_date =  response.xpath('//*[@class="entry-meta"]/p/text()').extract()[0].strip().replace("·","")
        like = 0
        bookmark = 0
        comment = 0
        content = response.xpath('//div[@class="entry"]').extract()[0]

        #处理点赞数为0的情况
        if response.xpath('//*[@class="post-adds"]/span[1]/h10/text()') == []:
            like = 0
        else:
            like = int(response.xpath('//*[@class="post-adds"]/span[1]/h10/text()').extract()[0])

        bookmark_origin = response.xpath('//*[@class="post-adds"]/span[2]/text()').extract()[0]
        comment_origin = response.xpath('//*[@class="post-adds"]/a/span[1]/text()').extract()[0]

        #使用正则表达式匹配收藏数评论数
        notNone = ".*?(\d+).*"
        match_obj = re.match(notNone, bookmark_origin)
        if match_obj:
            bookmark = int(match_obj.group(1))
        else:
            bookmark = 0

        match_obj = re.match(notNone, comment_origin)
        if match_obj:
            comment = int(match_obj.group(1))
        else:
            comment = 0

        #对tag标签进行预处理
        tag_list = response.xpath('//*[@class="entry-meta"]/p/a/text()').extract()
        pass
