# 1945. 간단한 소인수분해

t = int(input())

for i in range(t):

    num = int(input())
    timesList = []  # 제곱 수 리스트

    # 2의 소인수 구하기
    times = 0  # 제곱 수
    while (num % 2 == 0):
        num = num / 2 ####### 이 부분에서 시간 많이 써버림... 나누기를 안하고 계속 while문을 돌리니, 서버 에러나지.ㅜㅜㅜ
        times = times + 1

    # 테스트n번째의 소인수를 리스트에 삽입
    timesList.append(str(times))

    # 3의 소인수 구하기
    times = 0  # 제곱 수
    while (num % 3 == 0):
        num = num / 3
        times = times + 1

    # 테스트n번째의 소인수를 리스트에 삽입
    timesList.append(str(times))

    # 5의 소인수 구하기
    times = 0  # 제곱 수
    while (num % 5 == 0):
        num = num / 5
        times = times + 1

    # 테스트n번째의 소인수를 리스트에 삽입
    timesList.append(str(times))

    # 7의 소인수 구하기
    times = 0  # 제곱 수
    while (num % 7 == 0):
        num = num / 7
        times = times + 1

    # 테스트n번째의 소인수를 리스트에 삽입
    timesList.append(str(times))

    # 11의 소인수 구하기
    times = 0  # 제곱 수
    while (num % 11 == 0):
        num = num / 11
        times = times + 1

    # 테스트n번째의 소인수를 리스트에 삽입
    timesList.append(str(times))
    print("#" + str(i + 1), ' '.join(timesList))