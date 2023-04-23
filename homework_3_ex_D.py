n = int(input())
possible = set(range(1, n+1))
impossible = set()

while True:
    question = input()
    if question == 'HELP':
        break
    else:
        numbers = set(map(int, question.split()))
        answer = input()
        if answer == 'YES':
            possible.intersection_update(numbers)
        else:
            impossible.update(numbers)

print(*sorted(possible - impossible))


