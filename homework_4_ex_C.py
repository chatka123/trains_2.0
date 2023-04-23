ans = {}

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for i in lines:
        for word in i.split():
            if word not in ans.keys():
                ans[word] = 0
            ans[word] += 1

sort_ans = [(-value, key) for key, value in ans.items()]
sort_ans = sorted(sort_ans)
for i in sort_ans:
    print(i[1])