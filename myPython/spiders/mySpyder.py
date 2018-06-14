# -*- coding: utf-8 -*-
import scrapy


class MyspyderSpider(scrapy.Spider):
    name = 'mySpyder'
    allowed_domains = ['duozhuayu.com']
    start_urls = ['http://duozhuayu.com/']

    def parse(self, response):
        pass
