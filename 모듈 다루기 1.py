# 모듈 생성 (moduletest.py란 파일을 만든다)

def add(a,b):
    return a+b

def sub(a,b):
    return a-b
----------------
# 모듈 불러오기 (cmd창에서 입력)

>cd C:\Users\admin\Desktop\python test  # 파일 디렉토리로 이동
>dir				         # 디렉토리 안의 파일 리스트
>python

>>>import moduletest		         # 불러올 파일명 (띄어쓰기는 오류?)
>>>print(moduletest.add(3,4))
7
>>>print(moduletest.sub(4,2))
2				         # 모듈 불러온 후 사용 예제1
----------------
>>>from moduletest import add, sub
>>>add(3,4)
7				         # 모듈 불러온 후 사용 예제2
----------------
>>>from mod1 import *		         # 모듈의 모든 함수를 불러서 사용하겠다
----------------
# moduletest파일에

# if __name__ == "__main__":
#     print(add(1, 4))
#     print(sub(4, 2))

# 이 소스를 추가하면 그냥 실행했을 경우 추가된 if문장이 참이되어 수행되지만 대화형 인터프리터(>>>)에서 사용할 떄는 if문이 거짓이 되어 다음문장 수행되지 않음
