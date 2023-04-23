first = list(map(int, input().split()))
second = list(map(int, input().split()))

print(len(set(first).intersection(second)))
