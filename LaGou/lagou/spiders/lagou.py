# -*- coding: utf-8 -*-
import scrapy
from ..items import LagouItem
import logging
from scrapy import Request,FormRequest
from lagou import settings
import json


log = logging.getLogger(__file__)
class JobboleSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0']

    def __init__(self):
        self.headers = settings.HEADER
        self.cookies = settings.COOKIES

    login_url='https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'

    def start_requests(self):
        log.info('======执行POST请求=====')
        for num in range(1,15):
            fd = {'first': 'false',
              'pn': str(num),
              'kd': 'java'}
            yield FormRequest(self.login_url,
                          formdata=fd,
                          headers=self.headers,
                          cookies=self.cookies,
                          callback=self.parse)  # jump to login page


    def parse(self, response):
        log.info('=====解析当前页=====')
        # print(response.body.decode('utf-8'))
        dict = json.loads(response.body)
        content = dict['content']
        positionResult = content['positionResult']
        result_list = positionResult['result']
        for result in result_list:
            lagou = LagouItem()
            lagou['positionName'] = result['positionName']
            lagou['companyShortName'] = result['companyShortName']
            lagou['salary'] = result['salary']
            lagou['positionAdvantage'] = str(result['positionAdvantage'])
            yield lagou

    # def post_url(self,response,num):
    #     fd = {'first': 'false',
    #           'pn': num,
    #           'kd': 'java'}
    #     yield FormRequest.from_response(response,
    #                       formdata=fd,
    #                       headers=self.headers,
    #                       cookies=self.cookies,
    #                       callback=self.parse)  # jump to login page



        # for num in range(2,5):
        #     print('解析第{}页'.format(num))
        #     log.info('=====执行Post请求=====')
        #     fd = {'first': 'false',
        #           'pn': num,
        #           'kd': '爬虫'}
        #     yield FormRequest.from_response(response, formdata=fd, callback=self.parse)
        # pass




            # #
    # def POST(self, response,num):
    #     log.info('=====执行Post请求=====')
    #     fd={'first': 'false',
    #     'pn': num,
    #             'kd': '爬虫'}
    #     print(response)
    #     yield FormRequest.from_response(response, formdata=fd, callback=self.parse)


    # def parse_article(self,response):
    #     log.info('=====解析详情页=====')
    #     article = ArticlespiderItem()
    #     article['title'] = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
    #     article['date'] = response.xpath('//div[@class="entry-meta"]/p/text()').extract_first().strip()
    #     yield article
    #
    # def parse_next_url(self,response):
    #     log.info('=====解析下一页URL=====')
    #     next_url=response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
    #     # if next_url!=[]:
    #     return next_url