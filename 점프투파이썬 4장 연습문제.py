#점프 투 파이썬 4장 연습문제 1번

def is_odd (num):
    if num % 2 == 0: return print("짝수")
    else: return print("홀수")
-------------------------
#점프 투 파이썬 4장 연습문제 2번

def avg (*num):
    total = 0
    for i in num:
        total += i
    return total / len (num)

print(result)
----------------------
#점프 투 파이썬 4장 연습문제 3번

input1 = int(input("첫번째 숫자를 입력하세요:"))
input2 = int(input("두번째 숫자를 입력하세요:"))

total = input1 + input2
print("두 수의 합은 %s 입니다" % total)
------------------
#점프 투 파이썬 4장 연습문제 5번

with open("test.txt", 'w') as f1:
    f1.write("Life is too short! ")
with open("test.txt", 'r') as f2:
    print(f2.read())
--------------------------
#점프 투 파이썬 4장 연습문제 6번

user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   # 내용을 추가하기 위해서 'a'를 사용
f.write(user_input)
f.write("\n")               # 입력된 내용을 줄 단위로 구분하기 위해 줄 바꿈 문자 삽입
f.close()
--------------------------
#점프 투 파이썬 4장 연습문제 7번

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()
