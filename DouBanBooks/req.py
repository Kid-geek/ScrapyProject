import requests
from bs4 import BeautifulSoup

url='https://book.douban.com/top250?start=0'
html=requests.get(url).content.decode('utf-8')
soup=BeautifulSoup(html,'lxml')
div=soup.find('div',class_='indent')
table=div.find_all('table')
for item in table:
    url=item.find('a')['href']
    span=item.find('span',class_='inq').text
