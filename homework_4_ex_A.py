n = int(input())
ans = {}
for i in range(n):
    d, a = map(int, input().split())
    if d not in ans.keys():
        ans[d] = a
    else:
        ans[d] += a

keys = sorted(ans.items())
for i in keys:
    print(*i)
