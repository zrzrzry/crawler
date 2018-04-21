# -*- coding: utf-8 -*-
import scrapy


class FgoWikiMaterialSpider(scrapy.Spider):
    name = 'fgo_wiki_material'
    allowed_domains = ['docs.google.com/spreadsheets/']
    start_urls = ['https://docs.google.com/spreadsheets/d/e/2PACX-1vSgINV7TiiW1BklV4U0Ie1NngPpjJ0mZLn247UY36OP3gJk5NaezrSlADDLbPy2XIxXJo8c9Nte7tQL/pubhtml?gid=1739139175#']

    def parse(self, response):

        pass
