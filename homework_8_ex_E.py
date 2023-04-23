n = int(input())


for i in range(n):
    reply = []
    strin = list(input())
    tree = ['root', [None], [None]]
    ans = []
    for letter in strin:
        if letter == 'D':
            ans.append(str(0))
        else:
            reply.append(''.join(ans))
            while int(ans[-1]) != 0:
                del ans[-1]
            ans[-1] = str(1)
    else:
        reply.append(''.join(ans))
        print(len(reply))
        for i in reply:
            print(i)


