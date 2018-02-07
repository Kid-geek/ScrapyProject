from scrapy import cmdline
name='books'
cmd='scrapy crawl {}'.format(name)
cmdline.execute(cmd.split())