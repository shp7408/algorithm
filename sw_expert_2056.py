# 2056. 연월일 달력

t = int(input())

for i in range(1, t + 1):

    cal = input()

    year = int(cal[:4])
    month = int(cal[4:6])
    day = int(cal[6:8])
    # print(year, month, day)

    if month == 0 or month > 12 or day == 0:
        print("#" + str(i), "-1")

    elif month == 2:
        print(("#" + str(i) + " " + str(year).zfill(4) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)) if day <= 28 else (
                    "#" + str(i) + " -1"))

    elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        print(("#" + str(i) + " " + str(year).zfill(4) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)) if day <= 31 else (
                    "#" + str(i) + " -1"))

    elif month == 4 or month == 6 or month == 9 or month == 11:
        print(("#" + str(i) + " " + str(year).zfill(4) + "/" + str(month).zfill(2) + "/" + str(day).zfill(2)) if day <= 30 else (
                    "#" + str(i) + " -1"))


# 쉽지 않구만...
# 1. 요구사항 분석 : 문제 / 제약조건 파악
# 2. 설계 : 연필로 직접 적어보며, 작은 test case를 해결해보기
# 3. 구현 : 코딩 시작
# 4. 테스트
# 5. 유지 보수

#1 2222/2/28 -1
#2 -1
#3 101/1/1 -1
#4 -1
#5 1111/11/11 -1

#