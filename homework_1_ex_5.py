d = int(input())
x, y = map(int, input().split())

if x >= 0 and y >= 0 and x + y <= d:
    print(0)
else:
    dist = [(x ** 2 + y ** 2, 1), ((x - d) ** 2 + y ** 2, 2), (x ** 2 + (y - d) ** 2, 3)]
    min_ = min(dist)
    print(min_[1])
