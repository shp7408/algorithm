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
# 7. N개의 원소들의 인덱스 별로 체크
# 체크 방식!! 체크 횟수는 전체 N - K +1

T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())

    aList = []

    for i in range(N):
        a = input()
        a1 = a.replace(" ", "")
        aList.append(a1)

    firstLast = '0' * N  # 00000
    aList.append(firstLast)
    aList.insert(0, firstLast)

    bList = []
    for i in aList:
        i2 = "0" + i + "0"
        bList.append(i2)  # 0000000

    num = 0
    indexFNum = 0
    times = N - K + 1

    oneStr = "1"
    oneStr = "0" + oneStr * K + "0"

    for i in range(times + 1):
        for j in range(times + 1):
            if bList[i][j:j + times] == oneStr:
                print(f'#{case} {bList[i][j:j + times]}')
                num = num + 1

    # 문자열을 잘라서, 둘이 같은지를 확인하기

    colStr = ""  # oneStr 과 세로로 비교할 문자열

    for i in range(times + 1):
        for j in range(times + 1):

            colStr = colStr + bList[i][j]

            if colStr == oneStr:
                num = num + 1
                print("DDDD")

    print(f'#{case} {num}')


def check(li,n,s,e,k):
    global cnt
    if li[s][e:e+k] == [1]*k:
        if e+k == n and e != 0 and li[s][e-1] == 0:
            cnt += 1
        elif e+k < n and e == 0 and li[s][e+k] == 0:
            cnt += 1
        elif e+k < n and e != 0 and li[s][e+k] == 0 and li[s][e-1] == 0:
            cnt += 1
        return
    return

for tc in range(int(input())):
        N,K = map(int, input().split())
        puzzle = [list(map(int, input().split())) for _ in range(N)]
        puzzle_rev = [[puzzle[m][n] for m in range(N)] for n in range(N)]
        cnt = 0
for i in range(N):
    for j in range(N):
        check(puzzle,N,i,j,K)
        check(puzzle_rev, N, i, j, K)
    print("#{} {}".format(tc+1,cnt))