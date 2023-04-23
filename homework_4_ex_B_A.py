n, m = map(int, input().split())
table = []
for i in range(n):
    table.append(list(input()))

words = []
for i in range(m):
    words.append(input())
all_del = []
words = sorted(words)

for word in words:
    delete = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == word[0]:
                dx = [-1, 0, 1, 0]
                dy = [0, -1, 0, 1]
                delete.append((i, j))
                for k in range(1, len(word)):
                    found = False
                    for l in range(4):
                        x = i + dx[l]
                        y = j + dy[l]
                        if 0 <= x < n and 0 <= y < n and table[x][y] == word[k]:
                            i, j = x, y
                            delete.append((i, j))
                            found = True
                            break
                    if not found:
                        delete = []
                        break
                else:
                    all_del.extend(delete)

for koord in all_del:
    table[koord[0]][koord[1]] = 0
ans = []

for t in table:
    for i in t:
        if i != 0:
            ans.append(i)

print(''.join(ans))

# n, m = map(int, input().split())
# table = [input() for _ in range(n)]
# words = [input().strip() for _ in range(m)]
# print(table)
# letters = set(''.join(table))  # создаем множество из всех букв в таблице
# print(letters)
# # проходим по каждому ключевому слову
# for word in words:
#     # ищем все вхождения слова в таблицу
#     for i in range(n):
#         for j in range(n):
#             if table[i][j] == word[0]:
#                 # начало вхождения слова найдено
#                 # проверяем, есть ли остальные буквы слова в таблице
#                 dx = [-1, 0, 1, 0]  # смещения по x для проверки соседних клеток
#                 dy = [0, 1, 0, -1]  # смещения по y для проверки соседних клеток
#                 for k in range(1, len(word)):
#                     found = False
#                     for l in range(4):
#                         x = i + dx[l]
#                         y = j + dy[l]
#                         if 0 <= x < n and 0 <= y < n and table[x][y] == word[k]:
#                             # следующая буква слова найдена в соседней клетке
#                             i, j = x, y  # переходим к следующей клетке
#                             found = True
#                             break
#                     if not found:
#                         break
#                 else:
#                     # все буквы слова найдены в таблице
#                     # удаляем их из множества
#                     for letter in word:
#                         letters.discard(letter)
#
# # выводим оставшиеся буквы из множества
# print(''.join(sorted(letters)))