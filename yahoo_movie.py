import requests
import pandas as pd
from bs4 import BeautifulSoup

# define url for crawling
url = 'https://movies.yahoo.com.tw/chart.html'

resp = requests.get(url)
resp.encoding = 'utf-8'  # encoded with format utf-8 for chinese character
soup = BeautifulSoup(resp.text, 'lxml')
#print(soup)

# parse colname
rows = soup.find_all('div', class_='tr')
# print(rows)
# get strings and convert into list
colname = list(rows.pop(0).stripped_strings)
colname

# parse rest content info
contents = []
for row in rows:
    thisweek_rank = row.find_next('div', attrs={'class': 'td'})
    updown = thisweek_rank.find_next('div')
    lastweek_rank = updown.find_next('div')

    # for the data from of first row in this web page is defferent from other rows
    if thisweek_rank.string == str(1):
        movie_title = lastweek_rank.find_next('h2')
    else:
        movie_title = lastweek_rank.find_next('div', attrs={'class': 'rank_txt'})

    #print(movie_title)
    #print(type(movie_title))

    release_date=movie_title.find_next('div',attrs={'class':'td'})
    trailer=release_date.find_next('div',attrs={'class':'td'})
    trailer_address=trailer.find('a')['href']
    stars=row.find('h6',attrs={'class':'count'})

    # replace None with empty string ''
    lastweek_rank=lastweek_rank.string if lastweek_rank.string else ' '

    c=[thisweek_rank.string,lastweek_rank,movie_title.string,release_date.string,trailer_address,stars.string]
    # c=[thisweek_rank.string,lastweek_rank,movie_title.string]
    print(c)
    contents.append(c)

    #convert to data frame format

    df=pd.DataFrame(contents,columns=colname)
    df.head()
