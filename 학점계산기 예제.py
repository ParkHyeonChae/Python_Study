# 학점계산기 1

subject_number = int (input("총 과목수 : "))

total = 0

for i in range(subject_number):
    print (i+1,end='')
    score = str(input("번 과목 등급 : "))
    if score == "A+" or score == "a+": total += 4.5
    elif score == "A" or score == "a": total += 4
    elif score == "B+" or score == "b+": total += 3.5
    elif score == "B" or score == "b": total += 3
    elif score == "C+" or score == "c+": total += 2.5
    elif score == "C" or score == "c": total += 2
    elif score == "D+" or score == "d+": total += 1.5
    elif score == "D" or score == "d": total += 1
    elif score == "F" or score == "f": total += 0
   
print ("평균 학점 : ",total/subject_number)
