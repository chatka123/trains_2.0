string = list(input())

maxim = len(string[:len(string) // 2])
for a, b in zip(string[:len(string) // 2], string[:len(string) // 2:-1]):
    if a == b:
        maxim -= 1

print(maxim)