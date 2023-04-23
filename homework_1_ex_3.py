date = input().split()
x = int(date[0])
y = int(date[1])
year = int(date[2])

if x == y:
    print(1)
elif x <= 12 and y <= 12:
    print(0)
else:
    print(1)
