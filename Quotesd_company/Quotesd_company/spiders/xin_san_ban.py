# -*- coding: utf-8 -*-
import scrapy
import logging
from bs4 import BeautifulSoup
from ..items import QuotesdCompanyItem

log = logging.getLogger(__file__)
class Xin_San_Ban(scrapy.Spider):
    name = 'xin_san_ban'
    # allowed_domains = ['http://quote.eastmoney.com']
    # start_urls = ['https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0']

    custom_settings = {
        "COOKIES_ENABLED": False,
        'DEFAULT_REQUEST_HEADERS': {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        }
    }

    def start_requests(self):
        for num in range(1,2):
            url = 'http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._81.BASIC&sty=FCOIA&sortType=C&sortRule=-1&page='+str(num)+'&pageSize=20&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=44c9d251add88e27b65ed86506f6e5da&jsName=quote_123&_g=0.03720576056314151'
            log.info('======解析至:{}页====='.format(num))
            yield scrapy.Request(url,callback=self.parse)

    def parse(self, response):
        log.info('=====解析列表页=====')
        # print(response.body.decode('utf-8'))

        result=response.text.replace('var quote_123={rank:[','').replace('],pages:594}','')
        result = result.split('\"')
        for item in result:
            quote_info=QuotesdCompanyItem()
            if item == '':
                continue
            if item == ',':
                continue
            # print(item)
            share_name=item.split(',')[2]  # 股票名称
            share_id=item.split(',')[1]     # 股票id
            quote_info['share_name']=share_name
            quote_info['share_id'] = share_id
            info_url='http://quote.eastmoney.com/3ban/sz{}.html'.format(quote_info['share_id'])
            print(info_url)
            yield scrapy.Request(url=info_url,meta={'item': quote_info},callback=self.parse_info)

    def parse_info(self,response):
        html_soup=BeautifulSoup(response.text,'lxml')
        quote_info = response.meta['item']
        div=html_soup.find('div',id='gsjjbox')

        quote_info['company_name']=div.find_all('p')[1]['title']
        quote_info['company_attribute'] = div.find_all('p')[2].text.replace('公司属性：','')
        quote_info['operate_range'] = div.find_all('p')[4]['title']
        quote_info['create_time'] = div.find_all('span')[0].text
        quote_info['regis_money'] = div.find_all('span')[1].text
        quote_info['industry'] = div.find_all('span')[2].text
        quote_info['province'] = div.find_all('span')[3].text
        # print(quote_info)
        yield quote_info

