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

DOWNLOADER_MIDDLEWARES = {
   'lagou.middlewares.ProxyMiddleware': 543,
}


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

# 默认Item并发数：100
CONCURRENT_ITEMS = 100

# 默认Request并发数：16
CONCURRENT_REQUESTS = 16

# 默认每个域名的并发数：8
CONCURRENT_REQUESTS_PER_DOMAIN = 8

# 每个IP的最大并发数：0表示忽略
CONCURRENT_REQUESTS_PER_IP = 0

DOWNLOAD_TIMEOUT = 35
# DOWNLOAD_DELAY = 1  # 间隔时间

# REDIRECT_ENABLED = True #禁止重定向

#在此设置POST 的 URL
# px  排序方式: new  最新  default   默认
# gx  工作性质: 全职   实习
# gj  工作经验: 不限 应届毕业生 3年及以下 3-5年 5-10年 10年以上 不要求
#     工作经验为 应届毕业生时 URL为 'https://www.lagou.com/jobs/positionAjax.json?px=default&gx=全职&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=1'
POST_URL='https://www.lagou.com/jobs/positionAjax.json?gj=3年及以下&px=new&city=北京&needAddtionalResult=false&isSchoolJob=0'

# 在此设置要输入的职位关键字
POSITION='爬虫'

MYSQL_DB_NAME='lagou_scrapy'
MYSQL_HOST='localhost'
MYSQL_USER='root'
MYSQL_PASSWORD='123456'

# 在此设置要存入哪个表
MYSQL_TABLE_NAME='java_shixi'


ITEM_PIPELINES = {
   # 'ArticleSpider.pipelines.ArticlespiderPipeline': 300,
   #  'ArticleSpider.mysql_pipelines.MySQLPipeline':401,
    'lagou.pipemysql.MySQLAsyncPipeline': 401
    # 'lagou.mysql_pipe.MySQLPipeline': 401
}


HEADER={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Cookie':'JSESSIONID=ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA; _ga=GA1.2.145327400.1515463987; user_trace_token=20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644; LGUID=20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644; _gid=GA1.2.1007945172.1515463987; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515463987; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=b16b5e3154608ccb232953f358a2639d; LGSID=20180110165347-c52fdfcd-f5e3-11e7-8227-525400f775ce; X_MIDDLE_TOKEN=15cea09db2cd4031bcb52054dce69c85; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=c5ec6d7d733542249756aef288cec1dc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515576257; LGRID=20180110172420-09f44a21-f5e8-11e7-822a-525400f775ce'
        'Referer': 'https://www.lagou.com/jobs/list_java?px=new&city=%E5%8C%97%E4%BA%AC'
}

COOKIES={'JSESSIONID': 'ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA', ' _ga': 'GA1.2.145327400.1515463987', ' user_trace_token': '20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644', ' LGUID': '20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644', ' _gid': 'GA1.2.1007945172.1515463987', ' Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1515463987', ' index_location_city': '%E5%8C%97%E4%BA%AC', ' TG-TRACK-CODE': 'search_code', ' SEARCH_ID': '19da954bda14430e96bfbeb7e280917a', ' _gat': '1', ' LGSID': '20180109104920-b11805d6-f4e7-11e7-a021-5254005c3644', ' PRE_UTM': '', ' PRE_HOST': '', ' PRE_SITE': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D', ' PRE_LAND': 'https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC', ' Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6': '1515466160', ' LGRID': '20180109105141-0522d10d-f4e8-11e7-a021-5254005c3644'}