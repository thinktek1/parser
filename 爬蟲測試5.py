#抓八卦版指定日指定頁的爬蟲
import requests
from bs4 import BeautifulSoup
import  re
#import time

url='https://www.ptt.cc/bbs/Gossiping/index.html'
page=int(input("pls input page number:"))
day2=input('pls input date:')
#print(url)
for i in range(page):
    resq = requests.get(url,cookies={'over18':'1'}).text.encode('utf-8')
    soup = BeautifulSoup(resq, 'html.parser')
    #print(soup)
    sel=soup.select('div.r-ent')
    #print(sel)
    uppage=soup.select('div.btn-group.btn-group-paging a')[1]['href']
    list1=[]
    articles=[]
    for s in sel:
        try:
            title = s.find('a').text
            # print(title)
            href = "https://www.ptt.cc" + s.find('a')['href']
            # print(href)
            day1 = s.find('div', 'date').text.strip()
            # print(day1)
            # print(today)
            # print(day1)
            if (day2 == day1):
                list1 = [title, href, day1]
                articles.append(list1)
        except:
            None

    if len(articles) == 0:
        print("無資料")
    for article in articles:
        for i in article:
            print(i, end=" ")
        print()
    url = "https://www.ptt.cc" + uppage

