n = int(input())
num = sorted(list(map(int, input().split())))
k = int(input())


ans = []
for i in range(k):
    L, R = map(int, input().split())
    l = 0
    r = len(num) - 1
    while l < r:
        m = (l + r) // 2
        if num[m] >= L:
            r = m
        else:
            l = m + 1
    l0 = l
    r = len(num) - 1
    while l < r:
        m = (l + r + 1) // 2
        if num[m] <= R:
            l = m
        else:
            r = m - 1
    if l0 == r and num[l0] not in range(L, R + 1):
        ans.append(0)
    else:
        ans.append(l - l0 + 1)

print(*ans)



