num = list(map(int, input().split()))
previous = set()

for i in num:
    if i in previous:
        print('YES')
    else:
        print('NO')
    previous.add(i)


