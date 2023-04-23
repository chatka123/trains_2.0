TREE = [None]
num_levels = 0


def create_and_fill_node(tree, key):
    tree[0] = key
    tree.append([None])
    tree.append([None])


def find(tree, val):
    key = tree[0]
    if key == val:
        return True
    if key == None:
        return False
    elif val < key:
        left = tree[1][0]
        if left is None:
            return False
        else:
            return find(tree[1], val)
    elif val > key:
        right = tree[2][0]
        if right is None:
            return False
        else:
            return find(tree[2], val)


def add(tree, val):
    if find(tree, val):
        print('ALREADY')
    else:
        key = tree[0]
        if val < key:
            left = tree[1][0]
            if left is None:
                print('DONE')
                return create_and_fill_node(tree[1], val)
            else:
                return add(tree[1], val)
        elif val > key:
            right = tree[2][0]
            if right is None:
                print('DONE')
                return create_and_fill_node(tree[2], val)
            else:
                return add(tree[2], val)


def check_point(tree):
    key = tree[0]
    if key is None:
        return False
    else:
        return key


def check_left(tree):
    key = tree[1][0]
    if key is None:
        return False
    else:
        return key, tree[1]


def check_right(tree):
    key = tree[2][0]
    if key is None:
        return False
    else:
        return key, tree[2]


def print_tree(tree):
    ans = ['']
    prev_left_keys = [tree[0]]
    prev_right_keys = []
    prev_trees = [tree]
    reply = [(tree[0], '')]
    while True:
        if check_left(tree) is not False and check_left(tree)[0] not in prev_left_keys:
            key, tree = check_left(tree)
            prev_trees.append(tree)
            prev_left_keys.append(key)
            ans += '.'
            reply.append((key, ''.join(ans)))
        elif check_right(tree) is not False and check_right(tree)[0] not in prev_right_keys:
            key, tree = check_right(tree)
            prev_trees.append(tree)
            prev_right_keys.append(key)
            ans += '.'
            reply.append((key, ''.join(ans)))
        else:
            del prev_trees[-1]
            del ans[-1]
            if len(prev_trees) == 0:
                break
            tree = prev_trees[-1]
    reply.sort()
    for val, dots in reply:
        print(dots + str(val))







# def print_tree(tree):
#     ans = ['']
#     prev_keys = []
#     prev_trees = []
#     reply = []
#     for i in range(920):
#         if check_left(tree) is not False and check_left(tree) not in prev_keys:
#             reply.append((check_left(tree), ''.join(ans)))
#             prev_keys.append(check_left(tree))
#             prev_trees.append(tree)
#             tree = tree[1]
#             ans += '.'
#         elif tree[0] is None:
#             del prev_trees[-1]
#             del ans[-1]
#             tree = prev_trees[-1]
#         else:
#             while not check_right(tree) or check_right(tree)[0] in prev_keys:
#                 del prev_trees[-1]
#                 del ans[-1]
#                 tree = prev_trees[-1]
#                 if len(prev_trees) == 1:
#                     break
#             if check_right(tree):
#                 ans += '.'
#                 key, tree = check_right(tree)
#                 prev_trees.append(tree)
#             else:
#                 break
#     reply.sort()
#     for val, dots in reply:
#         print(dots + str(val))


with open('input.txt', 'r') as f:
    first_add = True
    for line in f:
        if line.split()[0] == 'ADD' and first_add:
            create_and_fill_node(TREE, int(line.split()[1]))
            first_add = False
            print('DONE')
        elif line.split()[0] == 'ADD':
            add(TREE, int(line.split()[1]))
        elif line.split()[0] == 'SEARCH':
            if find(TREE, int(line.split()[1])):
                print('YES')
            else:
                print('NO')
        else:
            print_tree(TREE)

with open('right_ans', 'r') as right, open('my_ans', 'r') as my:
    for r, m in zip(right, my):
        if r != m:
            print(r + m + 'FALSE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
