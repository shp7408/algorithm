# 1989. 초심자의 회문 검사

t = int(input())

for test in range(1, t + 1):
    strList = list(input())
    # print("strList : ", strList)

    # list 순서 바꾸기
    revList = list(reversed(strList))
    # print("revList : ", revList)

    print("#" + str(test) + " 1" if (strList == revList) else "#" + str(test) + " 0")