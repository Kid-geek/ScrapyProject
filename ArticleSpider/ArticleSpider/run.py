from scrapy import cmdline

name = 'jobbole'
cmd = "scrapy crawl {}".format(name)
cmdline.execute(cmd.split())
