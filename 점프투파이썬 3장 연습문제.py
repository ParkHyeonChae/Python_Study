#점프 투 파이썬 3장 연습문제 1번

a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
-------------------------
#점프 투 파이썬 3장 연습문제 2번

sum =0

i=1

while i<=1000:
    if i % 3 ==0:
        sum += i
    i+=1

print (sum)
------------------------------
#점프 투 파이썬 3장 연습문제 3번

i = 0

while True:
    i+= 1
    if i > 5: break
    print('*'*i)
---------------------
#점프 투 파이썬 3장 연습문제 4번

for i in range(1,101):
    print(i)
---------------------
#점프 투 파이썬 3장 연습문제 5번

student = [70,60,55,75,95,90,80,80,85,100]
total = 0

for score in student:
    total += score

avg = total/ len(student)
print(avg)
