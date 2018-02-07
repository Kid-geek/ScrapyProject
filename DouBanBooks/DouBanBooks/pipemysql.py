from twisted.enterprise import adbapi
from DouBanBooks import settings
from scrapy.utils.project import get_project_settings

# 异步 MYSQL

class MySQLAsyncPipeline(object):


    def __init__(self):
        setting=get_project_settings()
        db =  'douban'
        host = 'localhost'
        port =  3306
        user = 'root'
        passwd = '123456'
        self.table_name='books'
        self.dbpool=adbapi.ConnectionPool('MySQLdb',host=host,db=db,user=user,passwd=passwd,charset='utf8')

    def close_spider(self,spider):
        self.dbpool.close()

    def process_item(self,item,spider):
        self.dbpool.runInteraction(self.insert_db,item)
        return item

    def insert_db(self,tx,item):
        values=(item['name'],
        item['author'] ,
        item['commentary'],
        item['score'] ,
        item['pages'] ,
        item['introduce'] ,
        item['tages'] ,
        )
        sql='INSERT IGNORE INTO '+self.table_name+' (name, author, commentary, score, pages, introduce, tages) VALUES (%s, %s, %s, %s, %s, %s, %s)'
        tx.execute(sql,values)