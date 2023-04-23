n = int(input())

events = []
for i in range(n):
    t, l = map(int, input().split())
    events.append((t, 1))
    events.append((t + l, -1))
events.sort()


num_assembl = 0
numbers_assembl = 0
for time, event in events:
    if event == 1:
        num_assembl += 1
        numbers_assembl = max(num_assembl, numbers_assembl)
    else:
        num_assembl -= 1

print(numbers_assembl)

