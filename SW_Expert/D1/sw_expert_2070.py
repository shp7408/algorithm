# 2070. 큰 놈, 작은 놈, 같은 놈

a = input()
a = int(a)

for i in range(a):
    i1, i2 = input().split()

    if i1 > i2:
        print("#" + str(i + 1), ">")

    elif i1 < i2:
        print("#" + str(i + 1), "<")

    else:
        print("#" + str(i + 1), "=")