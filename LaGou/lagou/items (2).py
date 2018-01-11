# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LagouItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    companyId = scrapy.Field()      # 企业ID
    positionName = scrapy.Field()   # 职位名称
    workYear = scrapy.Field()       # 工作年限
    education = scrapy.Field()      # 学历
    jobNature = scrapy.Field()      # 工作性质
    positionId = scrapy.Field()     # 职位ID
    companyShortName = scrapy.Field()   # 公司简称
    createTime = scrapy.Field()     # 职位发布时间
    city = scrapy.Field()           # 公司所在城市
    salary = scrapy.Field()         # 薪水范围
    positionAdvantage = scrapy.Field()  # 职位优势
    district = scrapy.Field()        # 城区
    industryField = scrapy.Field()   # 行业
    companyFullName = scrapy.Field() # 公司全称
    financeStage = scrapy.Field()    # 融资情况
    industryField = scrapy.Field()   # 公司标签
    companySize = scrapy.Field()     # 员工人数
    info = scrapy.Field()
    pass
