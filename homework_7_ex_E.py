from math import pi

n = int(input())

r_min = 0
r_max = 10 ** 6
events = []
for i in range(1, n + 1):
    r1, r2, fi1, fi2 = map(float, input().split())
    r_min = max(r1, r_min)
    r_max = min(r_max, r2)
    events.append((fi1, -i))
    events.append((fi2, i))


events.sort()

current_open = 0
used = set()
for event in events:
    if event[1] < 0:
        current_open += 1
        used.add(-event[1])
    elif event[1] in used:
        current_open -= 1

ans = 0
for i in range(len(events)):
    event = events[i]
    if event[1] < 0:
        current_open += 1
    else:
        current_open -= 1
    if current_open == n:
        if i < len(events) - 1:
            ans += (events[i + 1][0] - events[i][0]) * (r_max ** 2 - r_min ** 2) / 2
        else:
            ans += (events[0][0] - events[len(events) - 1][0] + 2 * pi) * (r_max ** 2 - r_min ** 2) / 2

print(ans)