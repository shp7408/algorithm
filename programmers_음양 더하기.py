# 프로그래머스 / 레벨 1 / 음양 더하기

def solution(absolutes, signs):

    signsInt = list(map(int, signs))

    answer = sum([(absolutes[i]*(-1 if signsInt[i] == 0 else 1)
              ) for i in range (len(absolutes))])

    return answer