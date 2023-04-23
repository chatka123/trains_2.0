# n = int(input())
# num = list(map(int, input().split()))
#
# r = 1
#
# max_sum = min(num) - 1
# for l in range(len(num)):
#     current_sum = num[l]
#     while r < len(num) and num[r] + current_sum >= current_sum:
#         current_sum += num[r]
#         r += 1
#     if max_sum < current_sum:
#         max_sum = current_sum
#     if l + 2 < len(num):
#         r = l + 2
#
# print(max_sum)

# print((454376774 + 681211377 + 988713965) == max_sum)


n = int(input())
a = list(map(int, input().split()))
s = 0
mx = a[0]
for i in a:
    s += i
    mx = max(mx, s)
    if s < 0:
        s = 0
print(mx)
