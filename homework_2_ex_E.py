N = int(input())
number_of_grad = list(map(int, input().split()))
number_of_grad.sort()

print(sum(number_of_grad[:-1]))