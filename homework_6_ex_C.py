a, b, c, d = map(int, input().split())
f = lambda x: a * x ** 3 + b * x ** 2 + c * x + d
if d != 0:
    x = 0
    if d >= 0 and a > 0:
        r = x
        while f(x) >= 0:
            x -= d
        l = x - 1
        for i in range(100):
            m = (l + r) / 2
            if f(m) > 0:
                r = m
            else:
                l = m
        print(l)
    elif d >= 0 and a < 0:
        l = x
        while f(x) >= 0:
            x += d
        r = x + 1
        for i in range(100):
            m = (l + r) / 2
            if f(m) > 0:
                l = m
            else:
                r = m
        print(l)
    elif d < 0 and a < 0:
        r = x
        while f(x) <= 0:
            x -= - d
        l = x - 1
        for i in range(100):
            m = (l + r) / 2
            if f(m) > 0:
                l = m
            else:
                r = m
        print(l)
    elif d < 0 and a > 0:
        l = x
        while f(x) <= 0:
            x += - d
        r = x + 1
        for i in range(100):
            m = (l + r) / 2
            if f(m) > 0:
                r = m
            else:
                l = m
        print(l)
else:
    print(0)


































#
#
# a, b, c, d = map(int, input().split())
# f = lambda x: a * x ** 3 + b * x ** 2 + c * x + d
#
# eps = 0.00001
# x = 0
# dx = 10
#
# fx = f(x)
# fx_eps = f(x + eps)
# if fx < fx_eps <= 0:
#     l = x
#     while f(x) <= 0:
#         x += dx
#         dx *= 100
#     r = x
#     while l + eps < r:
#         x = (l + r) / 2
#         if f(x) > 0:
#             r = x
#         else:
#             l = x
#     print(x)
# elif fx > fx_eps <= 0:
#     r = x
#     print(f(x))
#     while f(x) <= 0:
#         print(f(x))
#         x += dx
#         dx *= 1000000
#     l = x
#     while l + eps < r:
#         x = (l + r) / 2
#         if f(x) < 0:
#             r = x
#         else:
#             l = x
#     print(f(x))
# elif fx > fx_eps >= 0:
#     l = x
#     while f(x) <= 0:
#         x += dx
#         dx *= 100
#     r = x
#     while l + eps < r:
#         x = (l + r) / 2
#         if f(x) > 0:
#             r = x
#         else:
#             l = x
#     print(x)
# elif fx < fx_eps >= 0:
#     r = x
#     while f(x) >= 0:
#         x -= dx
#         dx *= 100
#     l = x
#     while l + eps < r:
#         x = (l + r) / 2
#         if f(x) > 0:
#             r = x
#         else:
#             l = x
#     print(x)


