#점프 투 파이썬 5장 연습문제 8번

r = round(17/3,4)
print(r)
--------------------------
#점프 투 파이썬 5장 연습문제 9번

import sys

numbers = sys.argv[1:]

result = 0
for number in numbers:
    result += int(number)
print (result)
--------------------------
#점프 투 파이썬 5장 연습문제 10번

# os 모듈을 사용하여 다음과 같이 동작하도록 코드를 작성해 보자.
# 1.C:\doit 디렉터리로 이동한다.
# 2.dir 명령을 실행하고 그 결과를 변수에 담는다.
# 3.dir 명령의 결과를 출력한다.

>>> import os
>>> os.chdir("c:\doit")

>>> result = os.popen("dir")

>>> print (result.read())
--------------------------
#점프 투 파이썬 5장 연습문제 11번

# glob 모듈을 사용하여 C:\doit 디렉터리의 파일 중 확장자가 .py인 파일만 출력하는 프로그램을 작성

>>> import glob
>>> golb.glob("c:\doit\*.py")
--------------------------
#점프 투 파이썬 5장 연습문제 12번

# time 모듈을 사용하여 현재 날짜와 시간을 다음과 같은 형식으로 출력

>>> import time
>>> time.strftime("%Y/%m/%d %H:%M:%S")
--------------------------
#점프 투 파이썬 5장 연습문제 13번

# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성

import random

result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
