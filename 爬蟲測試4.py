#抓指定日指定頁的爬蟲
import requests
from bs4 import BeautifulSoup
url='https://www.ptt.cc/bbs/joke/index.html'
page=int(input("pls input page number:"))
day2=input('pls input date:')
for i in range(page):
    print(url)
    resq = requests.get(url).text.encode('utf-8')
    soup = BeautifulSoup(resq, 'html.parser')
    sel=soup.select('div.r-ent')
    uppage=soup.select('div.btn-group.btn-group-paging a')[1]['href']
    list1=[]
    articles=[]
    for s in sel:
        try:
            title=s.find('a').text
            href="https://www.ptt.cc"+s.find('a')['href']
            day1=s.find('div','date').text.strip()
            if (day2 == day1):
                list1=[title,href,day1]
                articles.append(list1)
        except:
            None
    if len(articles)==0:
        print("無資料")
    for article in articles:
        for i in article:
            print(i,end=" ")
        print()
    url = "https://www.ptt.cc" +uppage

