import pymysql

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='scrapy_db', charset='utf8')
    cursor = conn.cursor()
    rowNums = cursor.execute('SELECT * FROM article')
    print('查询的行数为' + str(rowNums))
    selectResultList = cursor.fetchall()
    print(type(selectResultList))
    # for i in range(len(selectResultList)):
    #     print(selectResultList[i])