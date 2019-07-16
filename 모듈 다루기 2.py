# 모듈 생성 (moduletest2.py란 파일을 만든다)

PI = 3.141592

class Math:
    def solv(self,r):
        return PI * (r ** 2)

def add (a, b):
    return a+b
----------------
# 모듈 불러오기 (cmd창에서 입력)

>cd C:\Users\admin\Desktop\python test  # 파일 디렉토리로 이동
>dir				         # 디렉토리 안의 파일 리스트
>python

>>>import moduletest2		         # 불러올 파일명 (띄어쓰기는 오류?)
>>>print(moduletest2)
3.141592                                 # PI변수를 활용
----------------
>>> a = moduletest2.Math()
>>> print(a.solv(2))
12.566368				 # Math클래스 사용하는 방법
----------------
>>> print(mod2.add(mod2.PI, 4.4))
7.541592		                 # Math클래스 안의 add함수 사용법
----------------

# 다른 파일에서 모듈 불러오기
# 1. 불러올 모듈이 있는 디렉토리에 새로운 파이썬 파일을 만든다
# 예시 (modtest.py 생성 후)

import moduletest2
result = moduletest2.add(3,4)
print(result)

