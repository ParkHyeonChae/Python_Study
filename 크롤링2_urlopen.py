# Section02-2
# 파이썬 크롤링 기초
# urlopen 함수 기초 사용법

import urllib.request as req
from urllib.error import URLError, HTTPError # 예외처리를 하기위해서 (서버의 정기점검, 잘못된 주소 등 오류를 대비하기 위해서)

# 다운로드 경로 및 파일명
path_list = ["C:/Users/HC/Desktop/test2.jpg", "C:/Users/HC/Desktop/index2.html"]

# 다운로드 리소스 URL
target_url = ["http://post.phinf.naver.net/20160621_169/1466482468068lmSHj_JPEG/If7GeIbOPZuYwI-GI3xU7ENRrlfI.jpg",
              "http://google.com"] #이미지, index

for i, url in enumerate(target_url): #2번 순회, enumerate는 리스트, 튜플, 문자열을 받는 함수
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url) # 서버에 요청을 하여 다운하지 않고 주소를 가져옴
        
        # 수신 내용
        contents = response.read() # response에서 read로 읽어와라, 읽어와서 contents 변수에 담는다

        print('---------------------------------------------------')

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('---------------------------------------------------')

        # 파일 쓰기
        with open(path_list[i], 'wb') as c:
            c.write(contents)

        # HTTP 에러 발생 시
    except HTTPError as e: # 서버가 죽어있거나, 404 에러 등 대비
        print("Download failed.")
        print('HTTPError Code : ', e.code)

        # URL 에러 발생 시
    except URLError as e:
        print("Download failed.")
        print('URL Error Reason : ', e.reason)

        # 성공
    else:
        print()
        print("Download Succeed.")
