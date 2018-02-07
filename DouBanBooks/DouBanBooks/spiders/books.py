import scrapy
from bs4 import BeautifulSoup
from ..items import DoubanbooksItem
import re

class DouBanBooks(scrapy.Spider):
    name = 'books'
    # allowed_domains = ['$domain']
    start_urls = ['https://book.douban.com/top250?start=0']
    def start_requests(self):
        for i in range(0,11):
            url='https://book.douban.com/top250?start={}'.format(i*25)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        div = soup.find('div', class_='indent')
        table = div.find_all('table')
        for item in table:
            url = item.find('a')['href']
            try:
                commentary = item.find('span', class_='inq').text
            except AttributeError:
                commentary=''
            yield scrapy.Request(url=url,meta={'commentary':commentary},callback=self.parse_info)

    def parse_info(self,response):
        item=DoubanbooksItem()
        item['name']=response.xpath('//*[@id="wrapper"]/h1/span/text()').extract_first().strip()
        item['author'] = response.xpath('//*[@id="info"]/a[1]/text()').extract_first().strip()
        item['commentary'] = response.meta['commentary']
        item['score'] = response.xpath('//*[@id="interest_sectl"]/div/div[2]/strong/text()').extract_first()
        item['pages'] = re.findall('页数:</span> ([0-9]*)',response.text)
        item['introduce'] = response.xpath('string(//div[@class="intro"])').extract_first().replace(' ','')
        item['tages'] = response.xpath('string(//*[@id="db-tags-section"]/div)').extract_first().strip().replace('  ',' ')
        yield item










