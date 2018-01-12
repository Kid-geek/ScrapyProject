import scrapy.cmdline

name='xin_san_ban'
cmd = "scrapy crawl {}".format(name)
scrapy.cmdline.execute(cmd.split())