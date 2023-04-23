# def check_children(family, first, second):
#     if first not in family.keys():
#         pass
#     else:
#         for name in family[first]:
#             if name == second:
#                 return True
#             else:
#                 check_children(family, name, second)
#     return False

def check_children(family, first, second):
    if first not in family.keys():
        return False
    if second in family[first]:
        return True
    else:
        for name in family[first]:
            if check_children(family, name, second):
                return True
    return False


with open('input.txt', 'r') as f:
    n = int(f.readline())
    family = {}
    for i in range(n - 1):
        son, father = f.readline().split()
        if father not in family.keys():
            family[father] = []
        family[father].append(son)
    for line in f:
        first, second = line.split()
        for father in family.keys():
            find_family = False
            if first == father:
                ans = check_children(family, first, second)
                if ans is True:
                    print(1)
                    find_family = True
                    break
            elif second == father:
                ans = check_children(family, second, first)
                if ans is True:
                    print(2)
                    find_family = True
                    break
        if not find_family:
            print(0)






