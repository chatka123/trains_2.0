n, m = map(int, input().split())
students = list(map(int, input().split()))
study = list(map(int, input().split()))

num_groups = 0
num_students = {}
num_study = {}
for i in range(1, len(students) + 1):
    if students[i - 1] not in num_students.keys():
        num_students[students[i - 1]] = []
    num_students[students[i - 1]].append(i)
    num_groups += 1

for i in range(1, len(study) + 1):
    if study[i - 1] != 1:
        if study[i - 1] not in num_study.keys():
            num_study[study[i - 1]] = []
        num_study[study[i - 1]].append(i)

sort_students = sorted(num_students.items(), key=lambda x: x[0])
sort_study = sorted(num_study.items(), key=lambda x: x[0])


l = 0
r = 0

if l < len(sort_students) and r < len(sort_study):
    count_groups = len(sort_students[l][1])
    count_classes = len(sort_study[r][1])

ans_zeros = [0] * num_groups
ans = []
for i in range(len(study)):
    if (l < len(sort_students) and r < len(sort_study)) and sort_students[l][0] + 1 <= sort_study[r][0]:
        if count_groups == count_classes:
            ans.append((sort_study[r][1], sort_students[l][1]))
            l += 1
            r += 1
            if l < len(sort_students) and r < len(sort_study):
                count_groups = len(sort_students[l][1])
                count_classes = len(sort_study[r][1])
            else:
                break
        elif count_groups > count_classes:
            ans.append((sort_study[r][1], sort_students[l][1][:count_classes]))
            r += 1
            del sort_students[l][1][:count_classes]
            if r < len(sort_study):
                count_groups -= count_classes
                count_classes = len(sort_study[r][1])
            else:
                break
        elif count_groups < count_classes:
            ans.append((sort_study[r][1][:count_groups], sort_students[l][1]))
            l += 1
            del sort_study[r][1][:count_groups]
            if l < len(sort_students):
                count_classes -= count_groups
                count_groups = len(sort_students[l][1])

            else:
                break
    else:
        r += 1
        if r < len(sort_study):
            count_classes = len(sort_study[r][1])
        else:
            break

for i in range(len(ans)):
    o = 0
    ind = ans[i][1]
    for j in ind:
        ans_zeros[j - 1] = ans[i][0][o]
        o += 1

otvet = 0
for i in ans_zeros:
    if i == 0:
        pass
    else:
        otvet += 1

print(otvet)
print(*ans_zeros)
