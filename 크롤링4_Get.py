# Section 03-1
# Get 방식 데이터 통신(1)

# encar 사이트 

import urllib.request
from urllib.parse import urlparse # url정보를 파싱할 때 사용

# encar사이트 기본 요청
url = "http://www.encar.com"
mem = urllib.request.urlopen(url)

print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(100).decode("utf-8")))
print('parse : {}'.format(urlparse("http://www.encar.co.kr?test=test").query))

# 기본 요청2(ipify)
API = "https://api.ipify.org"

# Get 방식 Parameter
values = {
    'format': 'json'
}

print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 URL 생성
url = API + "?" + params
print("요청 url= {}".format(url))

# 수신 데이터 읽기
data = urllib.request.urlopen(url).read()

# 수신 데이터 디코딩
text = data.decode("utf-8")
print('response : {}'.format(text))