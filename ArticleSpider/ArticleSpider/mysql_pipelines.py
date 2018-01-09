import MySQLdb

class MySQLPipeline:
    def open_spider(self,spider):
        db = spider.setting.get('MYSQL_DB_NAME', 'lagou_scrapy')
        host = spider.setting.get('MYSQL_HOST', 'localhost')
        port = spider.setting.get('MYSQL_PORT', 3306)
        user = spider.setting.get('MYSQL_USER', 'root')
        passwd = spider.setting.get('MYSQL_PASSWORD', '123456')

        self.db_conn=MySQLdb.connect('MySQLdb',host=host,db=db,user=user,passwd=passwd,charset='utf8')