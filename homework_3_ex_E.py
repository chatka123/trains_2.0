m = int(input())
people = {}

for i in range(1, m + 1):
    supp = set(input())
    people[i] = supp

n = int(input())
numbers = {}

for i in range(1, n + 1):
    number = input()
    count = 0
    for value in people.values():
        if set(number).intersection(value) == value:
            count += 1
    numbers[number, i] = count

for key in numbers.keys():
    if numbers[key] == max(numbers.values()):
        print(key[0])
