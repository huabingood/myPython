# -*- coding: utf-8 -*-
import scrapy


class MyspyderSpider(scrapy.Spider):
    name = 'qiye'
    # allowed_domains 是可以不写的
    # allowed_domains = ['duozhuayu.com']
    # 要爬取的起始路径
    start_urls = ['http://www.cnblogs.com/qiyeboy/category/793342.html']

    def parse(self, response):
        # 解析相关的内容并持久化
        # 获取该页面的 标题，时间，链接，阅读人数，评论人数
        fatherNodes = response.xpath('//*[@id="mainContent"]/div/div')
        for element in fatherNodes:
            date = element\
                .xpath('./[@id = "homepage1_HomePageDays_DaysList_ctl00_ImageLink"]/test()')\
                .extract_first()
            title = element\
                .xpath('./[ @ id = "homepage1_HomePageDays_DaysList_ctl00_DayList_TitleUrl_0"]/test()')\
                .extract_first()
            summary = element\
                .xpath('./[@id="mainContent"]/div/div[3]/div[3]/div/text()')\
                .extract_first()
            detailUrl = element\
                .xpath('./[@id="mainContent"]/div/div[3]/div[3]/div/a/@href')\
                .extract_first()
            # 提取出来的内容是这样的：posted @ 2018-05-23 16:57 七夜的故事 阅读(144) 评论(0)
            # 所以为了获取点赞人数和评论人数，必须对此进行提取
            need2Extract = element\
                .xpath('./[@id="mainContent"]/div/div[3]/div[5]/text()')\
                .extract_first()\
                .split(' ')
            # likeNum =


        # 获取下一页，并传递给自己继续处理
        netPage = response.xpath('//*[@id="nav_next_page"]/a/@href').extract_first()
        if netPage !='':
            yield scrapy.Request(url=netPage,callback=self.parse)