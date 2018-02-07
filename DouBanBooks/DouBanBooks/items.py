# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanbooksItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name= scrapy.Field()
    author= scrapy.Field()
    commentary= scrapy.Field()
    score= scrapy.Field()
    pages= scrapy.Field()
    introduce= scrapy.Field()
    tages= scrapy.Field()

    pass
