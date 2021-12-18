"""


날짜: 2021/08/30
이름: 강병화
내용: 파이썬 HTML 페이지 요청하기 실습

파싱(parsing) - 마크업 문서 (반정형)에서 특정 태그의 데이터를 추출처리하는 과정


"""

import requests as req
from bs4 import BeautifulSoup as bs

url = 'https://news.naver.com/main/home.naver'

html = req.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
#print(html)

# 페이지 파싱
dom = bs(html, 'html.parser')
titles = dom.select('#section_it > div.com_list > div > ul > li > a > strong')
# 5개를 리스트로 만듬 [<strong> ... </strong>,<strong> ... </strong>,<strong> ... </strong>,<strong> ... </strong>,<strong> ... </strong>]

# for title in titles:
#     print(title.text) # html태그에서 text만 뽑는다   title.string도 된다
# print(titles)

#다음 랭킹 뉴스 1위 ~ 5위 까지 출력
url_daum = 'https://news.daum.net/ranking/popular'
html_daum = req.get(url_daum).text

dom_daum = bs(html_daum, 'html.parser')
daum_titles = dom_daum.select('#mArticle > div.rank_news > ul.list_news2 > li > div.cont_thumb > strong > a')

for j in range(5):
    print('%d위 : %s' % (j+1, daum_titles[j].text))
