# Quiz 1.

class members:
    def __init__(self, name, age, phone):
        self.name = name
        self.age = age
        self.phone = phone
    def info(self):
        print(f"'가입하신 계정의 이름은 {self.name}이며 나이는 {self.age}세, 그리고 연락처는 {self.phone}입니다.'")

name = input('이름을 입력하세요: ')
age = input('나이를 입력하세여: ')
phone = input('전화번호를 입력하세요 (형식은 000-0000-0000) : ')

member = members(name, age, phone)

member.info()

# Quiz 2.

message = input('메시지를 입력하세요: ')
def length_of_message(message):
    a = len(message)
    if a <= 20:
        return '요금은 50원입니다.'
    elif a > 20:
        return '요금은 100원입니다.'

print (length_of_message(message))
