from scrapy import cmdline

name = 'lagou_all'
cmd = "scrapy crawl {}".format(name)
cmdline.execute(cmd.split())
