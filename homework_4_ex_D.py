parts = {}
all = 0
with open('input.txt', 'r') as f:
    for line in f:
        all += int(line.split()[-1])
        parts[' '.join(line.split()[0:-1])] = parts.get(' '.join(line.split()[0:-1]), 0) + int(line.split()[-1])

first_divide = all / 450

sum_votes = 0
for key, value in parts.items():
    parts[key] = [value, int(value // first_divide)]
    sum_votes += int(value // first_divide)


while sum_votes < 450:
    new_votes = {}
    for key, value in parts.items():
        new_votes[key] = (-(parts[key][0] % first_divide), parts[key][1])
    sort_new = sorted(new_votes, key=new_votes.get)
    for name in sort_new:
        parts[name][1] += 1
        sum_votes += 1
        if sum_votes == 450:
            break

for key, value in parts.items():
    print(key, value[1])

