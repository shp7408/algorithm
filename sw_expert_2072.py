# 2072. 홀수만 더하기

a = int(input())
list_str = []

for i in range(1, a + 1):
    list_str = input().split()
    # print(list_str)
    # print("#"+str(i))

    odd_result = 0  # 초기화 시켜야 하는 부분 체크해야 함

    for j in list_str:
        if int(j) % 2 != 0:  # 2로 나누었을 때, 나누어 떨어지지 않으면,
            odd_result += int(j)
            # print(int(j))

    print("#" + str(i), odd_result)