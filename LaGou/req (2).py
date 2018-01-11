import requests


# -*- coding: utf-8 -*-
# @Time    : 2017/7/5 10:31
# @Author  : atmon
# @Site    :
# @File    : abuyun_proxy.py
# @Software: PyCharm

def proxy():
    # 代理服务器
    proxyHost = "proxy.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyUser = "H55RA0Y147842O4D"
    proxyPass = "4FE078BC80525DB2"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }

    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }

    return proxies


def get_html(url):
    req = requests.session()
    print(url)
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Cookie': 'JSESSIONID=ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA; _ga=GA1.2.145327400.1515463987; user_trace_token=20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644; LGUID=20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644; _gid=GA1.2.1007945172.1515463987; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515463987; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=b16b5e3154608ccb232953f358a2639d; LGSID=20180110165347-c52fdfcd-f5e3-11e7-8227-525400f775ce; X_MIDDLE_TOKEN=15cea09db2cd4031bcb52054dce69c85; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=c5ec6d7d733542249756aef288cec1dc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515576257; LGRID=20180110172420-09f44a21-f5e8-11e7-822a-525400f775ce'
        # , 'Referer': 'https://www.lagou.com/jobs/list_java?px=new&city=%E5%8C%97%E4%BA%AC'
    }
    req.headers.update(Headers)
    # print(req.headers)
    resp = req.get(url=url, proxies=proxy(), timeout=25)
    html = resp.text
    # print(html)
    # 下载成功
    return html

def post_html(url,data):
    req = requests.session()
    print(url)
    Headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        # 'Cookie':'JSESSIONID=ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA; _ga=GA1.2.145327400.1515463987; user_trace_token=20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644; LGUID=20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644; _gid=GA1.2.1007945172.1515463987; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515463987; index_location_city=%E5%8C%97%E4%BA%AC; X_HTTP_TOKEN=b16b5e3154608ccb232953f358a2639d; LGSID=20180110165347-c52fdfcd-f5e3-11e7-8227-525400f775ce; X_MIDDLE_TOKEN=15cea09db2cd4031bcb52054dce69c85; _gat=1; TG-TRACK-CODE=index_search; SEARCH_ID=c5ec6d7d733542249756aef288cec1dc; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515576257; LGRID=20180110172420-09f44a21-f5e8-11e7-822a-525400f775ce'
    'Referer':'https://www.lagou.com/jobs/list_java?px=new&city=%E5%8C%97%E4%BA%AC'
    }
    req.headers.update(Headers)
    # print(req.headers)
    resp = req.post(url=url, proxies=proxy(),data=data ,timeout=25)
    html = resp.text
    # print(html)
    # 下载成功
    return html

if __name__ == '__main__':
    # url='https://www.lagou.com/jobs/2753102.html'
    # print(get_html(url))

    url='https://www.lagou.com/jobs/positionAjax.json?px=default&gx=全职&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=1'

    for num in range(1,2):
        fd = {'first': 'false',
              'pn': str(num),
              'kd': 'python'}
        print(post_html(url,fd))