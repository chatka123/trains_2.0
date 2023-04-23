n = int(input())
num = list(map(int, input().split()))
m = int(input())
req = list(map(int, input().split()))

ans =[]
for i in range(len(req)):
    req[i] = req[i], i
req.sort()
l = 0
for m_val, m_pose in req:
    r = len(num) - 1
    while l < r:
        o = (l + r) // 2
        if num[o] >= m_val:
            r = o
        else:
            l = o + 1
    l0 = l
    r = len(num) - 1
    while l < r:
        o = (l + r + 1) // 2
        if num[o] > m_val:
            r = o - 1
        else:
            l = o
    if l0 == l and num[l] != m_val:
        ans.append((m_pose, [0, 0]))
    else:
        ans.append((m_pose, [l0 + 1, l + 1]))
    l = l0

ans.sort()
for pose, val in ans:
    print(*val)