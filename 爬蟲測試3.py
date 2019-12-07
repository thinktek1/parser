#抓第一頁當日的爬蟲
import requests
from bs4 import BeautifulSoup
import time
url="https://www.ptt.cc/bbs/joke/index.html"
req=requests.get(url).text.encode('utf-8')
soup=BeautifulSoup(req,'html.parser')
today=time.strftime("%m/%d").lstrip('0')
#print(today)
sel=soup.select('div.r-ent')
list1=[]
articles=[]
#print(sel)
for s in sel:
    try:
        title=s.find('a').text
        href=s.find('a')['href']
        day1=s.find('div','date').text.strip()
        if (today == day1):
            list1=[title,href,day1]
            articles.append(list1)
    except:
        None
#print(articles)
for article in articles:
    for i in article:
        print(i,end=" ")
    print()

