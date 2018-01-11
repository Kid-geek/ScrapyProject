from scrapy import cmdline

name = 'lagou'
cmd = "scrapy crawl {}".format(name)
cmdline.execute(cmd.split())
