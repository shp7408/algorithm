# 1948. 날짜 계산기

def last_Date (month) :
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
        return 31
    elif month == 2 :
        return 28
    else :
        return 30


def sec_first_minus (first_Mon, fist_date, second_Mon, second_date) :

    if first_Mon == second_Mon :
        return second_date - fist_date + 1

    else :
        firstDate = last_Date(first_Mon) - fist_date  + 1

        middleDate = 0
        for month in range (first_Mon + 1 , second_Mon) :
            middleDate += last_Date(month)

        lastDate = second_date

        return firstDate + middleDate + lastDate

t = int(input())

for i in range (1, t+1) :
    firstAndSecondList = input().split()

    # firstAndSecondList 리스트를 int 형으로 변환
    line_int = list(map(int, firstAndSecondList))
    # 3 1 3 31

    print("#"+str(i), sec_first_minus(line_int[0], line_int[1], line_int[2], line_int[3] ))








# 개선 코드 1
T = int(input())
Month_info = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cntDay(m, d):
    for i in range(0, m - 1):
        d += Month_info[i]
    return d

for case in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    result = cntDay(m2, d2) - cntDay(m1, d1) + 1
    print(f'#{case} {result}')



# 개선 코드 2
for case in range(1, T+1):
    m1, d1, m2, d2 = map(int, input().split())
    d1 += sum(Month_info[:m1])
    d2 += sum(Month_info[:m2])
    result = d2 - d1 + 1
    print(f'#{case} {result}')



