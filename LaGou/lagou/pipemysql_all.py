from twisted.enterprise import adbapi
from lagou import settings
from scrapy.utils.project import get_project_settings

# 异步 MYSQL

class MySQLAsyncPipeline(object):


    def __init__(self):
        setting=get_project_settings()
        db = setting.get('MYSQL_DB_NAME', 'lagou_scrapy')
        host = setting.get('MYSQL_HOST', 'localhost')
        port = setting.get('MYSQL_PORT', 3306)
        user = setting.get('MYSQL_USER', 'root')
        passwd = setting.get('MYSQL_PASSWORD', '123456')
        self.table_name=settings.MYSQL_TABLE_NAME
        self.dbpool=adbapi.ConnectionPool('MySQLdb',host=host,db=db,user=user,passwd=passwd,charset='utf8')

    def close_spider(self,spider):
        self.dbpool.close()

    def process_item(self,item,spider):
        self.dbpool.runInteraction(self.insert_db,item)
        return item

    def insert_db(self,tx,itme):
        values=(itme['title'].replace('\'',''),
                itme['url'].replace('\'',''),
                itme['url_object_id'].replace('\'',''),
                itme['salary'].replace('\'',''),
                itme['job_city'].replace('\'',''),
                itme['work_years'],
                itme['degree_need'],
                itme['job_type'],
                itme['publish_time'],
                itme['job_advantage'],
                itme['job_desc'],
                itme['job_addr'],
                itme['company_name'],
                itme['company_url'],
                itme['tags'],
                itme['crawl_time']
        )
        sql='INSERT IGNORE INTO lagou_all (title, url, url_object_id, salary, job_city, work_years, degree_need, job_type, publish_time, job_advantage, job_desc, job_addr, company_name, company_url, tags, crawl_time) VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s", "%s")'
        tx.execute(sql,values)