seq = list(input())

r = 0

for l in range(len(seq)):
    if r < len(seq) and seq[l] == '(':
        while seq[r] != ')':
            r += 1
        r += 1
        if r == len(seq) and '(' not in seq[l + 1:]:
            result = True
            break
        else:
            result = False
    else:
        result = False


if result == True:
    print('YES')
else:
    print('NO')

