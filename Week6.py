def check_length_of_message(message):
    length = len(message)
    if length <= 20:
        return 50
    else:
        return 100

message = input("문자를 입력하시오: ")

money = check_length_of_message(message)

print(f'문자 요금은 {money}원입니다.')