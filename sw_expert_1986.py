# 1986. 지그재그 숫자

t = int(input())
# print("t:", t)
for i in range(1, t + 1):

    # num 까지 반복
    num = int(input())
    # print("num : ", num)

    # 더하거나, 뺄 값
    howNum = 0

    # 결과 낼 값
    answer = 0

    for j in range(1, num + 1):

        # 짝수인 경우
        if j % 2 == 0:
            howNum = -j
            # print("##" + str(j) + " : ", howNum)

            # 홀수인 경우
        else:
            howNum = j
            # print("##" + str(j) + " : ", howNum)

        answer = answer + howNum

    print("#" + str(i), answer)
