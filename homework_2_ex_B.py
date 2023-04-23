buildings = list(map(int, input().split()))

left = [0] * len(buildings)
shop = -20

for i in range(len(buildings)):
    if buildings[i] == 2:
        shop = i
    elif buildings[i] == 1:
        left[i] = i - shop

ans = 0
shop = 30
for i in range(len(buildings) - 1, -1, -1):
    if buildings[i] == 2:
        shop = i
    elif buildings[i] == 1:
        mindist = min(shop - i, left[i])
        ans = max(ans, mindist)

print(ans)