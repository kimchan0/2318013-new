# 1. 주어진 문자열 'Hello, World!'에서 첫 번째 단어 'Hello'만 추출하는 파이썬 코드를 작성하세요.

string='Hello, world!'
print(string[0:5])

# 2. 정수 7과 정수 3의 덧셈 값을 제곱하고, 이를 result 변수에 할당하는 파이썬 코드를 작성하세요.

result = (7 + 3) ** 2
print(result)

# 3. 주어진 리스트 A = [1, 2, 3, 4, 5]를 역순으로 하는 새로운 리스트 result = [5, 4, 3, 2, 1]를 만드시오.

result = []
results = [1, 2, 3, 4, 5]
result.append(results[4])
result.append(results[3])
result.append(results[2])
result.append(results[1])
result.append(results[0])
print(result)

# 4. 주어진 딕셔너리 {'apple': 3, 'banana': 5, 'cherry': 2}에서 'banana'의 값을 추출하는 파이썬 코드를 작성하세요.

Dictionary = {'apple': 3, 'banana': 5, 'cherry': 2}
print(Dictionary['banana'])
