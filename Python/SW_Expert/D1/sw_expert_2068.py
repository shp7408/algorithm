# 2068. 최대수 구하기

# 받은 테스트 케이스의 개수
a = input()
a = int(a)

# 개수만큼 반복문으로 행을 입력 받음
for i in range(0, a):

    bigNum = 0  # 가장 큰 수 초기화
    line = input().split()
    line_int = list(map(int, line))

    for j in range(0, 10):
        if line_int[j] > bigNum:
            bigNum = line_int[j]

    print("#" + str(i + 1), bigNum)