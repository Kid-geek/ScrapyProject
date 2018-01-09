import requests

if __name__ == '__main__':
    fd = {'first': 'false',
          'pn': '2',
          'kd': 'java'}
    login_url = 'https://www.lagou.com/jobs/positionAjax.json?px=new&city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'

    header={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
        'Cookie':'JSESSIONID=ABAAABAACBHABBIA187B7282557E66499A428644DA36BEA; _ga=GA1.2.145327400.1515463987; user_trace_token=20180109101307-a22bd30a-f4e2-11e7-a021-5254005c3644; LGUID=20180109101307-a22bd699-f4e2-11e7-a021-5254005c3644; _gid=GA1.2.1007945172.1515463987; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515463987; index_location_city=%E5%8C%97%E4%BA%AC; TG-TRACK-CODE=search_code; _gat=1; LGSID=20180109112312-6c65b5ea-f4ec-11e7-8139-525400f775ce; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_java%3Fpx%3Dnew%26city%3D%25E5%258C%2597%25E4%25BA%25AC; SEARCH_ID=76843b64dce94ac4a0780cd856649688; LGRID=20180109112323-72eae19f-f4ec-11e7-a022-5254005c3644; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1515468202'
        ,'Referer':'https://www.lagou.com/jobs/list_java?px=new&city=%E5%8C%97%E4%BA%AC'
    }

    html=requests.post(login_url,headers=header,data=fd).content.decode('utf-8')
    print(html)