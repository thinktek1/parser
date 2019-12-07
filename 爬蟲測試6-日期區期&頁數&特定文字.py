#抓指定日指定頁+指定日期區間+特定文字的爬蟲
import requests
from bs4 import BeautifulSoup
import csv
url='https://www.ptt.cc/bbs/joke/index.html'
page=int(input("pls input page number:"))
day1=int(input('pls input start date:').replace('/',''))
day2=int(input('pls input end date:').replace('/',''))
search_str=input('pls input search text:')
#print(day1,day2)
#print(type(day1),type(day2))

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
            current_day=int(s.find('div','date').text.strip().replace('/',''))
            if (day1<=current_day <= day2):
                if((search_str in title) or(search_str=='')):
                    #list1=[title,href,current_day]
                    #articles.append(list1)
                    print(title,href,current_day)
                    with open('joke6.txt','a') as fp:
                        fp.write(title)
                        fp.write(href)
                        fp.write(current_day)
                        fp.write('\n')
        except:
            None

    url = "https://www.ptt.cc" +uppage
