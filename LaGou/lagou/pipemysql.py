from twisted.enterprise import adbapi
import MySQLdb.cursors

from scrapy.utils.project import get_project_settings
class MySQLAsyncPipeline(object):


    def __init__(self):
        setting=get_project_settings()
        db = setting.get('MYSQL_DB_NAME', 'lagou_scrapy')
        host = setting.get('MYSQL_HOST', 'localhost')
        port = setting.get('MYSQL_PORT', 3306)
        user = setting.get('MYSQL_USER', 'root')
        passwd = setting.get('MYSQL_PASSWORD', '123456')

        self.dbpool=adbapi.ConnectionPool('MySQLdb',host=host,db=db,user=user,passwd=passwd,charset='utf8')

    def close_spider(self,spider):
        self.dbpool.close()

    def process_item(self,item,spider):
        self.dbpool.runInteraction(self.insert_db,item)
        return item

    def insert_db(self,tx,itme):
        values=(itme['positionName'],
                itme['companyShortName'],
                itme['salary'],
                itme['positionAdvantage'],
        )
        sql='INSERT IGNORE INTO java_beijing (positionName, companyShortName, salary, positionAdvantage) VALUES ("%s", "%s", "%s", "%s")'
        tx.execute(sql,values)