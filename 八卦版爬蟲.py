#抓當天日期joke版的的爬蟲
import requests
from bs4 import BeautifulSoup
import time
url = "https://www.ptt.cc/bbs/joke/index.html"
r = requests.get(url)
soup = BeautifulSoup(r.text,"html.parser")
sel = soup.find_all("div","r-ent") #標題
today = time.strftime("%m/%d").lstrip('0')
articles=[]
list1=[]
for s in sel: #印出網址跟標題
    title=s.find('a').text
    href='https://www.ptt.cc/'+s.find('a')['href']
    date=s.find('div','date').text.strip()
    #print(date)
    #print(today)
    #print(type(date))
    #print(type(today))
    if today == date:
    #    print("1")
        list1=[date,title,href]
    articles.append(list1)
    #url = "https://www.ptt.cc"+ u[1]["href"] #上一頁的網址
#print(sel)
for i in articles:
    for j in i:
        print(j,end=" ")
    print()
#print(articles)
