flag = True

numbers = []
while flag:
    num = int(input())
    if num == 0:
        flag = False
    numbers.append(num)

maximum = max(numbers)
count = 0
for i in numbers:
    if i == maximum:
        count += 1

print(count)
