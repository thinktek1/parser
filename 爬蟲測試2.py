#抓3頁joke版的爬蟲
import requests
from bs4 import BeautifulSoup

url='https://www.ptt.cc/bbs/joke/index.html'
for i in range(3):
    req=requests.get(url).text.encode('utf-8')
    soup=BeautifulSoup(req,'html.parser')
    sel=soup.select('div.title a')
    pre=soup.select('div.btn-group.btn-group-paging a')
    print(url)
    for s in sel:
        print(s.text,s['href'])
    url="https://www.ptt.cc"+pre[1]['href']
    #print(url)