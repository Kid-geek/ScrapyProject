# -*- coding: utf-8 -*-
import scrapy
from ..items import ArticlespiderItem
import logging
log = logging.getLogger(__file__)
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    # def start_requests(self):
    #     for num in range(1,2):
    #         url_page = 'http://blog.jobbole.com/all-posts/page/' + str(num) + '/'
    #         self.start_urls.append(url_page)
    #     for url in self.start_urls:
    #         yield self.make_requests_from_url(url)

    def parse(self, response):
        log.info('=====解析目录页=====')
        url_list = response.xpath('//span[@class="read-more"]/a/@href').extract()
        for url in url_list:
            yield scrapy.Request(url, callback=self.parse_article)

        next_url=self.parse_next_url(response)

        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)
        pass

    def parse_article(self,response):
        log.info('=====解析详情页=====')
        article = ArticlespiderItem()
        article['title'] = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first()
        article['date'] = response.xpath('//div[@class="entry-meta"]/p/text()').extract_first().strip()
        yield article

    def parse_next_url(self,response):
        log.info('=====解析下一页URL=====')
        next_url=response.xpath('//a[@class="next page-numbers"]/@href').extract_first()
        # if next_url!=[]:
        return next_url