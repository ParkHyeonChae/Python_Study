#for문 구구단 활용예제 

number= int(input("number = ")) # input은 들어올때 항상 문자열이기에 int로 묶어줌

for i in range(0,9):
   i=i+1
   print(number, " * ", i, " = ", i*number)

