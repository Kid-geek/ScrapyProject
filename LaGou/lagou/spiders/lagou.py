# -*- coding: utf-8 -*-
import scrapy
from ..items import LagouItem
import logging
from scrapy import Request,FormRequest
from lagou import settings
import json


log = logging.getLogger(__file__)
class LagouSpider(scrapy.Spider):
    name = 'lagou'
    allowed_domains = ['www.lagou.com']
    start_urls = ['https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0']

    #设置默认头  防封
    custom_settings = {
        "COOKIES_ENABLED": False,
        # "DOWNLOAD_DELAY": 1,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.8',
            'Connection': 'keep-alive',
            'Cookie': 'user_trace_token=20171015132411-12af3b52-3a51-466f-bfae-a98fc96b4f90; LGUID=20171015132412-13eaf40f-b169-11e7-960b-525400f775ce; SEARCH_ID=070e82cdbbc04cc8b97710c2c0159ce1; ab_test_random_num=0; X_HTTP_TOKEN=d1cf855aacf760c3965ee017e0d3eb96; showExpriedIndex=1; showExpriedCompanyHome=1; showExpriedMyPublish=1; hasDeliver=0; PRE_UTM=; PRE_HOST=www.baidu.com; PRE_SITE=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DsXIrWUxpNGLE2g_bKzlUCXPTRJMHxfCs6L20RqgCpUq%26wd%3D%26eqid%3Dee53adaf00026e940000000559e354cc; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; index_location_city=%E5%85%A8%E5%9B%BD; TG-TRACK-CODE=index_hotjob; login=false; unick=""; _putrc=""; JSESSIONID=ABAAABAAAFCAAEG50060B788C4EED616EB9D1BF30380575; _gat=1; _ga=GA1.2.471681568.1508045060; LGSID=20171015203008-94e1afa5-b1a4-11e7-9788-525400f775ce; LGRID=20171015204552-c792b887-b1a6-11e7-9788-525400f775ce',
            'Host': 'www.lagou.com',
            'Origin': 'https://www.lagou.com',
            'Referer': 'https://www.lagou.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def __init__(self):
        self.headers = settings.HEADER
        self.cookies = settings.COOKIES
        self.position= settings.POSITION

    login_url=settings.POST_URL

    def start_requests(self):

        # POST 列表URL
        for num in range(10,30):
            log.info('======解析至:{}====='.format(num))
            fd = {'first': 'false',
              'pn': str(num),
              'kd': self.position}
            yield FormRequest(self.login_url,
                          formdata=fd,
                          headers=self.headers,
                          # cookies=self.cookies,
                          callback=self.parse)  # jump to login page

    def parse(self, response):

        log.info('=====解析列表页=====')
        # print(response.body.decode('utf-8'))
        dict = json.loads(response.body)
        content = dict['content']
        positionResult = content['positionResult']
        result_list = positionResult['result']
        for result in result_list:
            lagou = LagouItem()
            lagou['positionName']= result['positionName']
            lagou['companyShortName']= result['companyShortName']
            lagou['salary']= result['salary']
            lagou['industryField']= result['industryField']
            lagou['positionAdvantage']= result['positionAdvantage']
            lagou['workYear']= result['workYear']
            lagou['education']= result['education']
            lagou['jobNature']= result['jobNature']
            lagou['positionId']= result['positionId']
            lagou['createTime']= result['createTime']
            lagou['city']= result['city']
            lagou['district']= result['district']
            lagou['companyFullName']= result['companyFullName']
            lagou['financeStage']= result['financeStage']
            lagou['companySize']= result['companySize']
            info_url='https://www.lagou.com/jobs/{}.html'.format(lagou['positionId'])
            print(info_url)
            yield scrapy.Request(url=info_url,meta={'item': lagou,'dont_redirect':True},headers=self.headers,callback=self.parse_info)

    # 解析详情页
    def parse_info(self,response):
        info=response.xpath('string(//dd[@class="job_bt"])').extract_first().strip()
        print(info)
        lagou = response.meta['item']
        lagou['info']=info
        yield lagou
