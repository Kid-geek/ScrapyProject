# -*- coding: utf-8 -*-

# Scrapy settings for lagou project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'lagou'

SPIDER_MODULES = ['lagou.spiders']
NEWSPIDER_MODULE = 'lagou.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'lagou (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
FEED_EXPORT_ENCODING = 'utf-8'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'lagou.middlewares.LagouSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'lagou.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'lagou.pipelines.LagouPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


MYSQL_DB_NAME='lagou_scrapy'
MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PASSWORD='123456'

ITEM_PIPELINES = {
   # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
   #  'ArticleSpider.mysql_pipelines.MySQLPipeline':401,
    'lagou.pipemysql.MySQLAsyncPipeline': 401
    # 'lagou.mysql_pipe.MySQLPipeline': 401
}


HEADER={
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
'Accept':'application/json, text/javascript, */*; q=0.01',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
'Host':'www.lagou.com',
'Origin':'https://www.lagou.com',
'Referer':'https://www.lagou.com/jobs/list_java?px=new&city=%E5%8C%97%E4%BA%AC',
'X-Anit-Forge-Code':0,
'X-Anit-Forge-Token':None,
'X-Requested-With':'XMLHttpRequest'
}

COOKIES={'JSESSIONID': 'ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA', ' _ga': 'GA1.2.145327400.1515463987', ' user_trace_token': '20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644', ' LGUID': '20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644', ' _gid': 'GA1.2.1007945172.1515463987', ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1515463987', ' index_location_city': '%E5%8C%97%E4%BA%AC', ' TG-TRACK-CODE': 'search_code', ' SEARCH_ID': '19da954bda14430e96bfbeb7e280917a', ' _gat': '1', ' LGSID': '20180109104920-b11805d6-f4e7-11e7-a021-5254005c3644', ' PRE_UTM': '', ' PRE_HOST': '', ' PRE_SITE': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D', ' PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC', ' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1515466160', ' LGRID': '20180109105141-0522d10d-f4e8-11e7-a021-5254005c3644'}