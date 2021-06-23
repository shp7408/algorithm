# 2007. 패턴 마디의 길이

T = int(input())

for case in range(1, T + 1):
    a = input()

    # a 문자열의 첫 문자와 같은 문자가 나올 때 까지, 반복문을 돌린다.
    first = a[0]
    second = a[0:2]
    howLong = 0
    for j in range(1, 10):
        howLong = howLong +1
        if first == a[j] :
            if second == a[j:j+2] :
                break
    print(f'#{case} {howLong}')







