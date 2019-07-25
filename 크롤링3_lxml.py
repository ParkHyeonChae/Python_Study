# Section02-3
# lxml 사용 기초 스크랩핑(1)

# parsing이란? : 구조에 맞게 원하는 데이터를 가져오는것

# lxml 사용 예제 - 네이버 뉴스 스탠드 스크랩핑

import requests # requests 모듈사용
import lxml.html # lxml의 html을 파싱

# 네이버 메인 뉴스 스크래핑 메인 함수
def main():
    response = requests.get("https://www.naver.com") # get으로 스크래핑 대상 url을 가져옴, get으로 요청
    # get방식과 post방식을 알아야함 (post는 보안이 강한 곳 ex은행)
    
    urls = scrape_news_list_page(response) # 신문사 링크를 받는 함수를 만듬

    for url in urls:
        print(url) # 결과출력
        # 이부분에서 파일쓰기를 할수 있음 (txt, 엑셀파일 등으로 저장)

def scrape_news_list_page(response): # 신문사 링크를 받는 함수 url부분을 파싱하는 코드

    urls =[] # url을 담을 리스트 선언
    root = lxml.html.fromstring(response.content) # 태그 정보 문자열 저장

    for a in root.cssselect(".api_list .api_item a.api_link > img"): # css선택자 공부 필수, 네이버뉴스의 개발자도구의 a태그의 공통된 부분을 가져온다
                            # 뜻 : api list하위의 item 하위의 a태그의 api link를 가진애들을 싹 가져와라
        url = a.get("alt") # href 속성 (개발자도구에서 확인)
        urls.append(url)

#    for a in root.cssselect(".api_list .api_item a.api_link > img"): # a link하위의 이미지태그를 가져오는법
#         url = a.get("alt") # alt 속성 (개발자도구에서 확인)
#         urls.append(url)
     
    return urls

if __name__ == '__main__':
    main()
    
# 어떤 정보를 추출할 것인지는 cssselect 안의 코드만 변경하면 됨 (copy selcet를 사용할수 없을 때(여러가지 정보 추출)
