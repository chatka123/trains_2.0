n, q = map(int, input().split())
num = list(map(int, input().split()))

pref_sums = [0] * (len(num) + 1)
for i in range(1, len(num) + 1):
    pref_sums[i] = pref_sums[i - 1] + num[i - 1]

print(pref_sums)

for i in range(q):
    l, r = map(int, input().split())
    print(pref_sums[r] - pref_sums[l - 1])