# 함수 정의 방법
# def function_name(parameter):
#     code

# 함수 호출
# function_name()
#-----------------
# 사용예제

def test(number):
    result = number * 100

    return result

num= test(int(input("정수를 입력: ")))
print (num)
#-----------------
# 매개변수에 따라 함수의 작동을 달리할때 *를 사용 

def args_func(*ags):
    print (ags)

args_func("kim")

# 튜플로 넘어오기에 

def args_func(*ags):
    for t in ags:
        print(t,end=' ')

args_func("kim","park")

# 이런 형태로 사용 가능
#-----------------
# *이 두개면 딕셔너리 형태로 받음

def kwargs_func(**kwargs):
    print(kwargs)

kwargs_func(n1="kim", n2="park", n3="lee")

# 딕셔너리로 넘어오기에

def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

kwargs_func(n1="kim", n2="park", n3="lee")

# 이 형태로 사용가능
#-----------------
# 응용

def ex(arg1, arg2, *args, **kwargs):  # *, **는 가변인자 (없어도됨)
    print(arg1, arg2, args, kwargs)

ex(10,20)
ex(10,20, "park","kim",age1=24,age2=35)
# 결과
10 20 () {}
10 20 ('park', 'kim') {'age1': 24, 'age2': 35}
#-----------------
# 중첩함수 (클로저)
# 함수 안에 함수가 있는 것

def nested_func(num):           # 2. num에 1000이 들어감
    def func_in_func(num):      # 3. 위의 num에서 1000이 전달되어 들어옴
        print('>>>', num)       # 6. 결과적으로 더해진 1000 출력
    print("in func")            # 4. in func 출력
    func_in_func(num + 1000)    # 5. 들어와있는 num에 1000을 더함

nested_func(1000)               # 1. nested_func에 1000을 입력
#-----------------
# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 메모리 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화

# 일반적 함수 -> 변수 할당
def mul(num : int) -> int:
    return num * 10

var_func = mul #메모리 할당
print(var_func(10))

# 람다식
lambda_mul = lambda num : num * 10 # num*10을 반환해라

print (lambda_mul(10))
#-----------------
# 람다식 활용
lambda_mul = lambda num : num * 10 # num*10을 반환해라

print (lambda_mul(10))

def func(x,y,fun):
    print (x*y*fun(10))

print(func(10,10,lambda x : x*1000)) # 이런식으로 메모리 낭비 방지


