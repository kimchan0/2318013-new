# Quiz 1.

a=input("문자열을 입력하세요: ")
if a =="안녕하세요":
    print("반갑습니다")
else:
    print("인사를 먼저하세요.")

# Quiz 2.

number = int(input("값을 입력하세요:"))
if number + 100 >= 150:
    print(number+100)
else:
    print("값이 부족합니다.")

# Quiz 3.

result = []
numbers = [100, 200, 300]
for a in numbers:
    n = a+(a*0.1)
    result.append(n)
print(result)

# Quiz 4.

results = []
numbers2 = [3, 100, 23, 33, 72, 94]
for q in numbers2:
    if q % 3 == 0:
        results.append(q)
print(results)

# Quiz 5.

counter = 1
while counter <= 1000:
    print(counter)
    counter = counter+1

# Quiz 6.

num = 1
r = []
while num <= 100:
    if num % 2 != 0:
        r.append(num)
    num += 1
print("홀수의 합:", sum(r))