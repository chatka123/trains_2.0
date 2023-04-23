L, K = map(int, input().split())
blocs = list(map(int, input().split()))

for i in range(len(blocs)):
    if L % 2 == 0:
        if blocs[i] == L / 2:
            print(blocs[i - 1], blocs[i])
            break
        elif blocs[i] > L / 2:
            print(blocs[i - 1], blocs[i])
            break
    else:
        if blocs[i] == L // 2:
            print(blocs[i])
            break
        elif blocs[i] > L // 2:
            print(blocs[i - 1], blocs[i])
            break

