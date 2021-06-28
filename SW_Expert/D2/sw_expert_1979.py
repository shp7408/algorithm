# 1979. 어디에 단어가 들어갈 수 있을까


# 1. 주어진 스트링을 배열로 변환
# 2. 행 0 / n+2 를 000... n+2로
# 3. 열 0 / n+2 를 000... n+2로
# 4. 행 중에 01110 문자열 체크
# 5. 열 중에 01110 문자열 체크
# 6. 체크해서 있을 때 마다, result+1

# 1. 한 줄 한 줄을 문자열 그대로 받는다.
# 2. 문자열의 공백을 제거한다.
# 3. 문자열을 리스트화 한다.
# 4. 문자열의 맨 앞, 맨 마지막을 0으로 감싼다.
# 5. 리스트화 된 문자열의 0 마지막 인덱스를 0*N 으로 감싼다.
# 6. 01110 체크
# 7.

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())

    aList = []

    for i in range(N):
        a = input()
        a1 = a.replace(" ", "")
        aList.append(a1)

    firstLast = '0'*N #00000
    aList.append(firstLast)
    aList.insert(0, firstLast)

    bList =[]
    for i in aList:
        i2 = "0" + i + "0"
        bList.append(i2)









