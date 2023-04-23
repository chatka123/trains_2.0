# s = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()[1:]))
#
# flag = True
# i = 1
# for u in range(len(a)):
#     if a[i] < s:
#         j = 1
#         for y in range(len(b)):
#             if b[j] + a[i] < s:
#                 if s - (b[j] + a[i]) in c:
#                     k = c.index(s - (b[j] + a[i]))
#                     print(i - 1, j - 1, k)
#                     exit()
#                 elif i == len(a) - 1:
#                     print(-1)
#                     exit()
#                 else:
#                     if j < len(b) - 1:
#                         j += 1
#                     else:
#                         i += 1
#                         j = 1
#             elif j < len(b) - 1:
#                 j += 1
#             else:
#                 i += 1
#                 break


# s = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
#
# i = j = k = 1
# n = len(b)
# m = len(c)
# found = False
#
# while i < len(a) and not found:
#     while j < n and a[i] + b[j] >= s:
#         j += 1
#     while k < m and a[i] + b[j - 1] + c[k] <= s:
#         if a[i] + b[j] + c[k] == s:
#             print(i - 1, j - 1, k - 1)
#             found = True
#             break
#         k += 1
#     i += 1
#     j = max(j - 1, 0)
#
# if not found:
#     print(-1)

def read_and_num():
    x = list(map(int, input().split()[1:]))
    for i in range(len(x)):
        x[i] = x[i], i
    x.sort()
    return x


s = int(input())
a = read_and_num()
b = read_and_num()
c = read_and_num()
c.sort(key=lambda x: (x[0], -x[1]))


flag = False
for a_val, a_pose in a:
    c_pose = len(c) - 1
    for b_val, b_pose in b:
        while c_pose > 0 and a_val + b_val + c[c_pose][0] > s:
            c_pose -= 1
        if a_val + b_val + c[c_pose][0] == s and (not flag or (a_pose, b_pose, c_pose) < ans):
            ans = a_pose, b_pose, c[c_pose][1]
            flag = True

if flag:
    print(*ans)
else:
    print(-1)









