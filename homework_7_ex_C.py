# # o = 0
# m = int(input())
#
# events = []
# while True:
#     l, r = map(int, input().split())
#     if l == r == 0:
#         break
#     else:
#         events.append((l, r))
#
# events.sort()
# r_prev = events[0][0] - 1
# l = events[0][0] - 1
# r = 0
# ans = [(l, r)]
# for left, right in events:
#     if right >= r and o >= left >= l:
#         l = left
#         r = right
#         del ans[-1]
#         ans.append((l, r))
#     elif r >= left and right > r:
#         change_prev = True
#         if r_prev >= left >= l:
#             del ans[-1]
#             change_prev = False
#         if change_prev:
#             r_prev = r
#         r = right
#         l = left
#         ans.append((l, r))
#     if ans[0][1] >= o and ans[-1][1] >= m:
#         break
#
#
# if ans[-1][1] < m:
#     print('No solution')
# else:
#     print(len(ans))
#     for i in ans:
#         print(*i)
#
#


def main():
    """
    Для чтения входных данных необходимо получить их
    из стандартного потока ввода (sys.stdin).
    Данные во входном потоке соответствуют описанному
    в условии формату. Обычно входные данные состоят
    из нескольких строк.
    Можно использовать несколько методов:
    * input() -- читает одну строку из потока без символа
    перевода строки;
    * sys.stdin.readline() -- читает одну строку из потока,
    сохраняя символ перевода строки в конце;
    * sys.stdin.readlines() -- вернет список (list) строк,
    сохраняя символ перевода строки в конце каждой из них.
    Чтобы прочитать из строки стандартного потока:
    * число -- int(input()) # в строке должно быть одно число
    * строку -- input()
    * массив чисел -- map(int, input().split())
    * последовательность слов -- input().split()
    Чтобы вывести результат в стандартный поток вывода (sys.stdout),
    можно использовать функцию print() или sys.stdout.write().
    Возможное решение задачи "Вычислите сумму чисел в строке":
    print(sum(map(int, input().split())))
    """
    # Читаем две строки из стандартного потока ввода


    j = input().strip()
    s = input().strip()

    # Инициализируем переменную для подсчета количества драгоценностей
    count = 0

    # Для каждого символа строки S проверяем, является ли он драгоценностью
    for stone in s:
        if stone in j:
            count += 1

    # Выводим количество найденных драгоценностей в стандартный поток вывода
    print(count)

if __name__ == '__main__':
    main()
