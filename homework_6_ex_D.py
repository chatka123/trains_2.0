def check_condition(day, params):
    a, k, b, m, x = params
    if (day - day // k) * a + (day - day // m) * b < x:
        return True
    return False


def binary_search(l, r, check, params):
    while l < r:
        day = (l + r) // 2
        if check(day, params):
            l = day + 1
        else:
            r = day
    return l


a, k, b, m, x = map(int, input().split())
l = 0
r = 2 * x // a
ans = binary_search(l, r, check_condition, (a, k, b, m, x))
print(ans)


