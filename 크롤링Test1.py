# 네이버 실시간 검색어 크롤링

import requests
from bs4 import BeautifulSoup as bs

req = requests.get('http://naver.com') # 사이트지정 naver에 요청
html = req.text # 요청한 사이트의 url의 html내용을 가져온다
soup = bs(html, 'html.parser') # 파싱
newest = soup.select('span.ah_k') # ah_k인 태그를 selector로 지정

count=0 # 20위까지 표시를 위해
for news in newest:
    count+=1
    print(str(count)+"위 : "+news.text)
    if count == 20: break
