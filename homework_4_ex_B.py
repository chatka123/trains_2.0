ans = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    print()
    for i in lines:
        if i.split()[0] not in ans.keys():
            ans[i.split()[0]] = int(i.split()[1])
        else:
            ans[i.split()[0]] += int(i.split()[1])

for i, a in sorted(ans.items()):
    print(i, a)
