# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QuotesdCompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    share_name= scrapy.Field()
    share_id= scrapy.Field()
    company_name= scrapy.Field()
    company_attribute = scrapy.Field()
    operate_range= scrapy.Field()
    create_time= scrapy.Field()
    regis_money= scrapy.Field()
    industry= scrapy.Field()
    province= scrapy.Field()
    pass


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    date = scrapy.Field()
    pass

