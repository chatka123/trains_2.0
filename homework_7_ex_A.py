n = int(input())
event = []
for i in range(n):
    l, r = map(int, input().split())
    event.append((l, r))

event.sort()
l0, r0 = event[0]
ans = r0 - l0
for i in range(1, len(event)):
    l, r = event[i]
    if r0 >= l >= l0 and r >= r0:
        ans += r - r0
        r0 = r
    elif l > r0:
        l0 = l
        r0 = r
        ans += r0 - l0

print(ans)
