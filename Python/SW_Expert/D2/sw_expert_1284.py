# 1284. 수도 요금 경쟁

test = int(input())

for i in range(1, test + 1):
    list = input().split()
    print(list)

    #    p = int(list[0])
    #    q = int(list[1])
    #    r = int(list[2])
    #    s = int(list[3])
    #    w = int(list[4])
    test = int(input())

    for i in range(1, test + 1):

        # map 에 int 와 리스트를 넣으면, 리스트의 모든 요소를 int를 사용하여, 변환
        p, q, r, s, w = map(int, input().split())

        A = p * w
        B = (s * (w - r) + q) if w >= r else q

        print('#', end='')
        print(i, end=' ')
        print(min(A, B))