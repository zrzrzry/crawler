# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#文件保存使用避免很多编码问题
import codecs
import json

from scrapy.pipelines.images import ImagesPipeline

class SpiderPipeline(object):
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article_json', 'w', encoding="utf-8")
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False)
        return item

class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for success, value in results:
            image_path = value["path"]
        item["front_image_path"] = image_path

        return item
