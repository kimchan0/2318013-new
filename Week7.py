# 로또 번호 생성 함수

import random

def random_lotto():
    result = []
    while len(result) < 6:
        num = random.randint(1, 45)
        if num not in result:
            result.append(num)
    return result

print(random_lotto())

# 구구단 클래스 작성

class math:
    def __init__(self, num):
        self.num = num
    def output(self):
        for i in range(1, 10):
            print(f'{self.num} X {i} = {self.num * i}')

a = math(int(input('몇 단을 불러올까요? : ')))
a.output()