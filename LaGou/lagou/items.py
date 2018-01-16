# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst,MapCompose,Join
from w3lib.html import remove_tags
import hashlib

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


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()

def remove_splash(value):
    # 去掉工作城市的斜线
    return value.replace('/','')

def handle_jobaddr(value):
    addr_list=value.split('\n')
    addr_list=[item.strip() for item in addr_list if item.strip()!='查看地图']
    return ''.join(addr_list)


class LagouItemLoader(ItemLoader):
    # 自定义ItemLoader
    default_output_processor = TakeFirst()

class MooclagouItem(scrapy.Item):
    # 拉勾网职位信息
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    url_object_id=scrapy.Field()
    salary=scrapy.Field()
    job_city=scrapy.Field(
        input_processor=MapCompose(remove_splash)
    )
    work_years=scrapy.Field(input_processor=MapCompose(remove_splash))
    degree_need=scrapy.Field(input_processor=MapCompose(remove_splash))
    job_type=scrapy.Field()
    publish_time=scrapy.Field()
    job_advantage=scrapy.Field()
    job_desc=scrapy.Field()
    job_addr=scrapy.Field(input_processor=MapCompose(remove_tags,handle_jobaddr))
    company_name=scrapy.Field()
    company_url=scrapy.Field()
    tags=scrapy.Field(
        input_processor=Join(',')
    )
    crawl_time=scrapy.Field()
    # crawl_update_time=scrapy.Field()
    pass
