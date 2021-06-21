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

        firstDate = 0
        firstDate = last_Date(first_Mon) - fist_date  + 1
        #print("firstDate ", firstDate)

        middleDate = 0
        for month in range (first_Mon + 1 , second_Mon) :
            middleDate += last_Date(month)
            #print(month, last_Date(month))

        #print("middleDate ",middleDate)


        lastDate = 0
        lastDate = second_date
        #print("lastDate ",lastDate)


        return firstDate + middleDate + lastDate

t = int(input())

for i in range (1, t+1) :
    firstAndSecondList = input().split()

    # firstAndSecondList 리스트를 int 형으로 변환
    line_int = list(map(int, firstAndSecondList))

    print("#"+str(i), sec_first_minus(line_int[0], line_int[1], line_int[2], line_int[3] ))