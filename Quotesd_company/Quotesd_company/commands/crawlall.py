#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017/9/22 15:34
# @Descript: 同时运行多个scrapy爬虫的几种方法（自定义scrapy项目命令） http://www.cnblogs.com/rwxwsblog/p/4578764.html

import logging
from scrapy.commands import ScrapyCommand, UsageError
from scrapy.crawler import CrawlerRunner
from scrapy.utils.conf import arglist_to_dict

log = logging.getLogger(__file__)

class Command(ScrapyCommand):
    requires_project = True

    def syntax(self):
        return '[options]'

    def short_desc(self):
        return 'Runs all of the spiders'

    def add_options(self, parser):
        ScrapyCommand.add_options(self, parser)
        parser.add_option("-a", dest="spargs", action="append", default=[], metavar="NAME=VALUE",
                          help="set spider argument (may be repeated)")
        parser.add_option("-o", "--output", metavar="FILE",
                          help="dump scraped items into FILE (use - for stdout)")
        parser.add_option("-t", "--output-format", metavar="FORMAT",
                          help="format to use for dumping items with -o")

    def process_options(self, args, opts):
        ScrapyCommand.process_options(self, args, opts)
        try:
            opts.spargs = arglist_to_dict(opts.spargs)
        except ValueError:
            raise UsageError("Invalid -a value, use -a NAME=VALUE", print_help=False)

    def run(self, args, opts):
        # settings = get_project_settings()

        spider_loader = self.crawler_process.spider_loader
        for spidername in args or spider_loader.list():
            log.info("*********cralall spidername************" + spidername)
            self.crawler_process.crawl(spidername, **opts.spargs)

        self.crawler_process.start()

"""
    二、让几个spider同时运行起来
　　现在我们的项目有两个spider，那么现在我们怎样才能让两个spider同时运行起来呢？你可能会说写个shell脚本一个个调用，也可能会说写个python脚本
    一个个运行等。然而我在stackoverflow.com上看到。的确也有不上前辈是这么实现。然而官方文档是这么介绍的。
"""
"""
import scrapy
from scrapy.crawler import CrawlerProcess
class MySpider(scrapy.Spider):
    # Your spider definition
    ...

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})

process.crawl(MySpider)
process.start() # the script will block here until the crawling is finished
"""

# Running multiple spiders in the same process
"""
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider1(scrapy.Spider):
    # Your first spider definition
    ...

class MySpider2(scrapy.Spider):
    # Your second spider definition
    ...

process = CrawlerProcess()
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start() # the script will block here until all crawling jobs are finished
"""

# 通过CrawlerRunner
"""
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider1(scrapy.Spider):
    # Your first spider definition
    ...

class MySpider2(scrapy.Spider):
    # Your second spider definition
    ...

configure_logging()
runner = CrawlerRunner()
runner.crawl(MySpider1)
runner.crawl(MySpider2)
d = runner.join()
d.addBoth(lambda _: reactor.stop())

reactor.run() # the script will block here until all crawling jobs are finished
"""

# 通过CrawlerRunner和链接(chaining) deferred来线性运行
"""
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider1(scrapy.Spider):
    # Your first spider definition
    ...

class MySpider2(scrapy.Spider):
    # Your second spider definition
    ...

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider1)
    yield runner.crawl(MySpider2)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished
"""

# 运行命令  scrapy crawlall