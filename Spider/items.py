# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ArticleItem(scrapy.Item):
    title = scrapy.Field()
    create_date = scrapy.Field()
    like = scrapy.Field()
    bookmark = scrapy.Field()
    comment = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    front_image_url = scrapy.Field()
    front_image_path = scrapy.Field()
    tag_list = scrapy.Field()
pass

#定义servant item类将数据存入pipeline
class ServantItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    name_jp = scrapy.Field()
    name_en = scrapy.Field()
    image_url = scrapy.Field()
    image_path = scrapy.Field()
    servant_class = scrapy.Field()
    lv1_hp = scrapy.Field()
    lv1_atk = scrapy.Field()
    lvmax4_hp = scrapy.Field()
    lvmax4_atk = scrapy.Field()
    t_prop = scrapy.Fieldq()