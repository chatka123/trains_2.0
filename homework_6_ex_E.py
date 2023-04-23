def check_num(points, l):
    count = 0
    current_r = points[0] - 1
    for point in points:
        if point > current_r:
            count += 1
            current_r = point + l
    return count


n, k = map(int, input().split())
points = sorted(list(map(int, input().split())))

left = 0
right = points[-1] - points[0]

while left < right:
    l = (left + right) // 2
    if k >= check_num(points, l):
        right = l
    else:
        left = l + 1
print(left)




