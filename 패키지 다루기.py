# 패키지(Package)란? : 도트(.)를 사용하여 파이썬 모듈을 계층적으로 관리

# 1. 패키지 만들기
# 디렉토리에 다음의 서브 디렉토리와 파일들을 생성
# 사용예제 

C:\Users\HC\Desktop\Python Test\game\_init_.py
C:\Users\HC\Desktop\Python Test\game\sound\_init_.py
C:\Users\HC\Desktop\Python Test\game\sound\echo.py
C:\Users\HC\Desktop\Python Test\game\graphic\_init_.py
C:\Users\HC\Desktop\Python Test\game\graphic\render.py

# echo.py
def echo_test():
    print ("echo")

# render.py
def render_test():
    print ("render")

# game 패키지를 참조할 수 있도록 cmd에서 set 명령어로 PYTHONPATH환경변수에 디렉토리 추가

>set PYTHONPATH = C:\Users\HC\Desktop\Python Test
>python
-----------------------------
# 2. 패키지 안의 함수 실행하기
# 패키지 안의 함수를 실행하는 방법은 3가지가 있다. 예제를 실행하고 나서는 인터프리터 종료 후 재실행(Ctrl + z)

# 2.1 import하여 실행

>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo

# 2.2 실행할 모듈의 디렉토리까지를 from .... import하여 실행

>>> from game.sound import echo
>>> echo.echo_test()
echo

# 2.3 모듈의 함수를 직접 import하여 실행

>>> from game.sound.echo import echo_test
>>> echo_test()
echo

# import a.b.c 처럼 import할때 가장 마지막 항목인 c는 반드시 모듈 또는 패키지여야 함
# _init_.py의 용도 : 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 함.
# python 3.3 버전부터는 init 파일이 없어도 패키지로 인식한다
-----------------------------
# 3. relative 패키지
# 디렉토리의 한 모듈이 다른 디렉토리의 모듈을 사용하고 싶을 떄 사용
# 예제 (graphic 디렉토리의 render모듈이 sound의  echo모듈을 사용할 때 다음과 같이 render를 수정)

from game.sound.echo import echo_test
def render_test():
    print ("render")
    echo_test()

# from game.sound.echo import echo_test 대신 from ..sound.echo import echo_test 사용하면 relactive하게 import
# (..) : 부모 디렉토리
# (..) 접근자는 모듈안에서만 사용하여야 함
