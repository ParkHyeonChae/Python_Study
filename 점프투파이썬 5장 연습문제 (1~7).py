#점프 투 파이썬 5장 연습문제 1번

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
--------------------------
#점프 투 파이썬 5장 연습문제 2번

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50) # 50 더하기
cal.add(60) # 60 더하기

print(cal.value)
--------------------------
#점프 투 파이썬 5장 연습문제 4번

list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3]))
--------------------------
#점프 투 파이썬 5장 연습문제 7번

a = [-8, 2, 7, 5, -3, 5, 0, 1]
max(a) + min(a)
