# 2071. 평균값 구하기

t = int(input())
list_str = []

for i in range(1, t + 1):
    list_str = input().split()
    # print(list_str)

    sum = 0

    for j in list_str:
        sum += int(j)

    print("#" + str(i), round(sum / 10))  # 파이썬 내장함수 반올림 메서드 round()
