def check_father(family, father, fathers):
    if father not in family.keys():
        return True, fathers
    else:
        fathers.append(family[father])
        if check_father(family, family[father], fathers):
            return True, fathers


with open('input.txt', 'r') as f:
    n = int(f.readline())
    family = {}
    for i in range(n - 1):
        son, father = f.readline().split()
        family[son] = father
    for line in f:
        first, second = line.split()

        fathers_first = [first]
        fathers_first = check_father(family, first, fathers_first)[1]
        # print(first, fathers_first)

        fathers_second = [second]
        fathers_second = check_father(family, second, fathers_second)[1]
        # print(second, fathers_second)
        for i in fathers_first:
            if i in fathers_second:
                print(i)
                break