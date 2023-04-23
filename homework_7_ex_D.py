n, o = map(int, input().split())
kats_points = list(map(int, input().split()))
kats_points.sort()

for i in range(o):
    L, R = map(int, input().split())
    l = 0
    r = len(kats_points) - 1
    while l < r:
        m = (l + r) // 2
        if kats_points[m] >= L:
            r = m
        else:
            l = m + 1
    l0 = l
    r = len(kats_points) - 1
    while l < r:
        m = (l + r + 1) // 2
        if kats_points[m] <= R:
            l = m
        else:
            r = m - 1
    if kats_points[l0] >= L and kats_points[r] <= R:
        r0 = r + 1
        print(r0 - l0)
    else:
        print(0)
    # if r == l0:
    #     r0 = r
    # else:
    #     r0 = r + 1
    # print(r0 - l0)

# n, m = map(int, input().split())
# kats_points = list(map(int, input().split()))
# kats_points.sort()
# events = [(kats_points[0], 0, 0)]
#
# pref_sum = [0]
# previ_val = kats_points[0]
# pref_inc = 0
# for point in kats_points:
#     if point == previ_val:
#         pref_inc += 1
#     else:
#         events.append((point, 0, 0))
#         pref_sum.append(pref_inc)
#         pref_inc += 1
#         previ_val = point
# else:
#     pref_sum.append(pref_inc)
#
# points = sorted(set(kats_points))
#
# open_events = events.copy()
# close_events = events.copy()
# for i in range(m):
#     l, r = map(int, input().split())
#     open_events.append((l, -1, i))
#     close_events.append((r, 1, i))
#
# open_events.sort()
# close_events.sort(reverse=True)
#
#
# ans = [[0, 0] for i in range(10 ** 5)]
# current_open = []
# current_close = []
# cond = False
# for point, event, ind in open_events:
#     if event == -1:
#         cond = True
#         current_open.append(ind)
#     elif event == 0 and cond:
#         pr_sum = pref_sum[points.index(point)]
#         for opens in current_open:
#             ans[opens][1] = pr_sum
#         current_open.clear()
#         cond = False
# cond = False
# for point, event, ind in close_events:
#     if event == 1:
#         cond = True
#         current_close.append(ind)
#     elif event == 0 and cond:
#         pr_sum = pref_sum[points.index(point) + 1]
#         for closes in current_close:
#             ans[closes][0] = pr_sum
#         current_close.clear()
#         cond = False
#
# index = 0
# for i in ans[:m]:
#     print(i[0] - i[1])


# pref_sum = [0]
# previ_val = kats_points[0]
# pref_inc = 0
# for point in kats_points:
#     if point == previ_val:
#         pref_inc += 1
#     else:
#         events.append((point, 0, 0))
#         pref_sum.append(pref_inc)
#         pref_inc += 1
#         previ_val = point
# else:
#     pref_sum.append(pref_inc)
#
# points = sorted(set(kats_points))
#
# open_events = events.copy()
# close_events = events.copy()
# for i in range(m):
#     l, r = map(int, input().split())
#     open_events.append((l, -1, i))
#     close_events.append((r, 1, i))
#
# open_events.sort()
# close_events.sort(reverse=True)
#
#
# ans = [[0, 0] for i in range(10 ** 5)]
# current_open = []
# current_close = []
# cond = False
# for point, event, ind in open_events:
#     if event == -1:
#         cond = True
#         current_open.append(ind)
#     elif event == 0 and cond:
#         pr_sum = pref_sum[points.index(point)]
#         for opens in current_open:
#             ans[opens][1] = pr_sum
#         current_open.clear()
#         cond = False
# cond = False
# for point, event, ind in close_events:
#     if event == 1:
#         cond = True
#         current_close.append(ind)
#     elif event == 0 and cond:
#         pr_sum = pref_sum[points.index(point) + 1]
#         for closes in current_close:
#             ans[closes][0] = pr_sum
#         current_close.clear()
#         cond = False
# print('good')
# index = 0
# for i in ans[:m]:
#     print(i[0] - i[1])
    # cond = False
    # events.append((l, -1))
    # events.append((r, 1))
    # events.sort()
    # for ind, event in events:
    #     if event == -1:
    #         cond = True
    #     elif event == 0 and cond:
    #         l = points.index(ind)
    #         cond = False
    #         break
    # for ind, event in events[::-1]:
    #     if event == 1:
    #         cond = True
    #     elif event == 0 and cond:
    #         r = points.index(ind) + 1
    #         break
    # print(pref_sum[r] - pref_sum[l])
    # events = copy_events.copy()

# q = [[1, 1]] * 10 **5
# q[0][0] = 10
# print(q[:10])










# for i in range(m):
#     l, r = map(int, input().split())
#     events.append((l, i, -1))
#     events.append((r, i, 1))

# events.sort()
# print(events)
# pref_sum = []
# pref_increment = 0
# prev_point = events[0][0]
# for point, event in events:
#     if point == prev_point:
#         pref_increment += 1
#     else:
#         pref_sum.append(pref_increment)
#         pref_increment += 1
#         prev_point = point
# else:
#
# print(pref_sum)

# for i in range(1, n + 1):
#     if i < len(kats_points) - 1 and kats_points[i] == kats_points[i + 1]:
#         pref_increment += 1
#     else:
#         pref_increment += 1
#         pref_sum.append((pref_increment, i))

# print(pref_sum)

# open = []
# point = 0
# for edge, ind, event in events:
#     if event == 0 and point != 0:
#         open.append(edge)
#         point = 0
#     elif event == -1:
#         point += 1
#         open.append()
# point = 0
# close = []
# for ind, event in events[::-1]:
#     if event == 0 and point != 0:
#         close.append(ind)
#         point = 0
#     elif event == 1:
#         point += 1
#
# print(open)
# print(close)



# # pref_kats = [0] * (n + 2)
# # for i in range(1, n + 2):
# #     pref_kats[i] = pref_kats[i - 1] + kats[i - 1]


#
# n, m = map(int, input().split())
# kats_points = list(map(int, input().split()))
# kats_points.sort()
#
# pref_sum = [(0, 0)]
# pref_increment = 0
# for i in range(n):
#     if i < len(kats_points) - 1 and kats_points[i] == kats_points[i + 1]:
#         pref_increment += 1
#     else:
#         pref_increment += 1
#         pref_sum.append((pref_increment, i))
#
# for i in kats_points:
#     kats[i] += 1
#
# pref_kats = [0] * (n + 2)
# for i in range(1, n + 2):
#     pref_kats[i] = pref_kats[i - 1] + kats[i - 1]
#
# for i in range(m):
#     l, r = map(int, input().split())
#     print(pref_kats[r + 1] - pref_kats[l])

#
# n, m = map(int, input().split())
# kats_points = list(map(int, input().split()))
# kats_points.sort()
# kats = [0] * (n + 1)
#
# for i in kats_points:
#     kats[i] += 1
#
# pref_kats = [0] * (n + 2)
# for i in range(1, n + 2):
#     pref_kats[i] = pref_kats[i - 1] + kats[i - 1]
#
# for i in range(m):
#     l, r = map(int, input().split())
#     print(pref_kats[r + 1] - pref_kats[l])