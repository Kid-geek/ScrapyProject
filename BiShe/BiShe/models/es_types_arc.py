# -*- coding: utf-8 -*-
__author__ = 'bobby'

from datetime import datetime
from elasticsearch_dsl import DocType, Date, Nested, Boolean, \
    analyzer, Completion, Keyword, Text, Integer

from elasticsearch_dsl.analysis import CustomAnalyzer as _CustomAnalyzer

from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=["localhost"])

class CustomAnalyzer(_CustomAnalyzer):
    def get_analysis_definition(self):
        return {}


ik_analyzer = CustomAnalyzer("ik_max_word", filter=["lowercase"])

class ArticleType(DocType):
    #伯乐在线文章类型
    suggest = Completion(analyzer=ik_analyzer)
    title = Text(analyer='ik_max_word')
    url = Keyword()
    url_object_id = Keyword()
    salary = Keyword()
    job_city = Keyword()
    work_years = Keyword()
    degree_need = Text(analyer='ik_max_word')
    job_type = Text(analyer='ik_max_word')
    publish_time = Keyword()
    job_advantage = Text(analyer='ik_max_word')
    job_desc = Text(analyer='ik_max_word')
    job_addr = Keyword()
    company_name = Text(analyer='ik_max_word')
    company_url = Keyword()
    tags = Text(analyer='ik_max_word')
    crawl_time = Date()

    class Meta:
        index = 'lagou'
        doc_type = 'possion'

if __name__ == "__main__":
    ArticleType.init()
