# Quiz 1.

def add(a, b, c, d):
    return a + b + c + d
def multiply(a, b, c, d):
    return a * b * c * d

print(add(1, 2, 3, 4))
print(multiply(1, 2, 3, 4))

# Quiz 2.

def odd_or_even(number):
    if number % 2 == 0:
        return '짝수'
    else:
        return '홀수'

print(odd_or_even(5))
print(odd_or_even(8))

# Quiz 3.

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)

print(calculate_average([10, 20, 30, 40, 50]))

# Quiz 4.

class Game:
    def __init__(self, name, gender, job):
        self.name = name
        self.gender = gender
        self.job = job

    def attack(self):
        print("공격!")

character = Game("Player", "Male", "Warrior")
character.attack()

#  Quiz 5.

class 부동산:
    def __init__(self, 위치, 평수, 종류, 가격, 준공년도):
        self.위치 = 위치
        self.평수 = 평수
        self.종류 = 종류
        self.가격 = 가격
        self.준공년도 = 준공년도
    def 정보(self):
        print(self.위치, ",", self.평수, ",", self.종류, ",", self.가격, ",", self.준공년도)

부동산 = 부동산('청주', '34평', '아파트', '7억', "2001")
부동산.정보()