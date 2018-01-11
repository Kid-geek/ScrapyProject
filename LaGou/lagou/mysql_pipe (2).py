import MySQLdb.cursors
from scrapy.utils.project import get_project_settings

# 同步MYSQL

class MySQLPipeline(object):

    def open_spider(self,spider):
        setting=get_project_settings()
        db = setting.get('MYSQL_DB_NAME', 'lagou_scrapy')
        host =  setting.get('MYSQL_HOST', 'localhost')
        port =  setting.get('MYSQL_PORT', 3306)
        user =  setting.get('MYSQL_USER', 'root')
        passwd =  setting.get('MYSQL_PASSWORD', '123456')

        self.db_conn=MySQLdb.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset='utf8')
        self.db_cur=self.db_conn.cursor()


    def close_spider(self,spider):
        self.db_conn.commit()
        self.db_conn.close()

    def process_item(self,item,spider):
        self.insert_db(item)
        return item

    def insert_db(self,itme):
        values=(itme['positionName'],
                itme['companyShortName'],
                itme['salary'],
                itme['positionAdvantage'],
        )
        sql='INSERT INTO java_beijing (positionName, companyShortName, salary, positionAdvantage) VALUES ("%s", "%s", "%s", "%s")'
        self.db_cur.execute(sql,values)