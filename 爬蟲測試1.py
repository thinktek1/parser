#爬joke版的最後一頁
import requests
from bs4 import BeautifulSoup
#fp=open('joke.txt',"w")
req=requests.get("https://www.ptt.cc/bbs/joke/index.html")
#print(req)
soup=BeautifulSoup(req.text.encode('utf-8'),'html.parser')
#print(soup)
sel=soup.select('div.title a')
#print(sel)
for s in sel:
    #with open('joke.txt','a') as fp:
    print(s.text,s['href'])
        #fp.write(s.text)
        #fp.write(s['href'])
        #fp.write('\n')



