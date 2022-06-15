# 1966. 숫자를 정렬하자

T = int(input())

for case in range(1, T + 1):
    num = int(input())

    # str 타입과 int 타입의 리스트의 경우, 정렬 방식이 다름
    numList = list(map(int, input().split()))
    numList.sort()
    numList = list(map(str, numList))

    print(f'#{case}', ' '.join(numList))







