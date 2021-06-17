# 1284. 수도 요금 경쟁

test = int(input())

for i in range(1, test + 1):
    list = input().split()
    print(list)

    p = int(list[0])
    q = int(list[1])
    r = int(list[2])
    s = int(list[3])
    w = int(list[4])

    if p * w <= q:
        print("#" + str(i), p * w)

    elif w < r and q < p * w:
        print("#" + str(i), q)

    elif w >= r and (s * w) + q < p * w:
        print("#" + str(i), (s * w) + q)

    else:
        print("#" + str(i), p * w, q, w, r, q, p * w, (s * w) + q)
