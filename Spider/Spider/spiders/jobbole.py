# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        #获取每一页中的具体文章的url并交给scrapy进行下载
        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
            image_url = post_node.css('img::attr(src)').extract()
            post_url = post_node.css("::attr(href)").extract()
            yield Request(url = post_url, meta = {"front_image_url":image_url}, callback = self.parse_detail)
            print(post_url)

        #提取下一页url
        next_url = response.css('.margin-20 a.next::attr(href)').extract()
        if next_url:
           yield Request(url = next_url, callback = self.parse)

    def parse_detail(self, response):
        #对文章具体内容字段的处理

        front_image_url = response.meta.get("image_url","")
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
