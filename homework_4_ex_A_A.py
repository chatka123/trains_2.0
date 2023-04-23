n = int(input())
s = list(input())

letters = {}
for i in s:
    if i not in letters:
        letters[i] = 0
    letters[i] += 1

alphabetical_letters = dict(sorted(letters.items()))

ans = []
for key, value in alphabetical_letters.items():
    if value / 2 >= 1:
        ans.append(key * (value // 2))
        alphabetical_letters[key] -= (value // 2) * 2

if 1 in alphabetical_letters.values():
    for key, value in alphabetical_letters.items():
        if value != 0:
            ans.append(key)
            answer = ans + ans[-2::-1]
            print(''.join(answer))
            break
else:
    answer = ans + ans[::-1]
    print(''.join(answer))

