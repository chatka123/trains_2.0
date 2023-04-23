num = list(map(int, input().split()))
dct = {}

for i in num:
    if i not in dct.keys():
        dct[i] = 1
    else:
        dct[i] += 1

ans = []
for key in dct.keys():
    if dct[key] == 1:
        ans.append(key)

print(*ans)