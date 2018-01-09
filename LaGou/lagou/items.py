# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # companyId = scrapy.Field()
    positionName = scrapy.Field()
    # workYear = scrapy.Field()
    # education = scrapy.Field()
    # jobNature = scrapy.Field()
    # positionId = scrapy.Field()
    companyShortName = scrapy.Field()
    # createTime = scrapy.Field()
    # city = scrapy.Field()
    salary = scrapy.Field()
    positionAdvantage = scrapy.Field()
    # financeStage = scrapy.Field()
    pass
