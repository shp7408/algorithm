# 1979. 어디에 단어가 들어갈 수 있을까


# 1. 주어진 스트링을 배열로 변환
# 2. 행 0 / n+2 를 000... n+2로
# 3. 열 0 / n+2 를 000... n+2로
# 4. 행 중에 01110 문자열 체크
# 5. 열 중에 01110 문자열 체크
# 6. 체크해서 있을 때 마다, result+1



T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())

    aList = []
    zeroList = []
    twoTwoList = []

    for i in range(N):
        zeroList.append('0')

    #print(zeroList)

    for i in range(N):
        aList = input().split()
        twoTwoList.append(aList)


    twoTwoList.insert(0, zeroList)
    twoTwoList.append(zeroList)
    print(case, twoTwoList[N+1])

    for i in range(N+2):
        twoTwoList[i].append('0')
    print(case, twoTwoList[0])















