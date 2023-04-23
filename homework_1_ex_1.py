# final_code = int(input().rstrip())
# iter_answer = int(input().rstrip())
# check_answer = int(input().rstrip())
#
# if iter_answer not in [0, 1, 4, 6, 7]:
#     print(iter_answer)
# else:
#     if (iter_answer == 0 or iter_answer == 4) and final_code != 0:
#         print(3)
#     elif iter_answer == 0 and final_code == 0:
#         print(check_answer)
#     elif iter_answer == 4 and final_code == 0:
#         print(4)
#     elif iter_answer == 1:
#         print(check_answer)
#     elif iter_answer == 6:
#         print(6)
#     elif iter_answer == 7:
#         print(1)


r = int(input())
i = int(input())
c = int(input())

if i == 0:
    if r != 0:
        print(3)
    else:
        print(c)
elif i == 1:
    print(c)
elif i == 4:
    if r != 0:
        print(3)
    else:
        print(4)
elif i == 6:
    print(0)
elif i == 7:
    print(1)
else:
    print(i)

