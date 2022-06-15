# 1288. 새로운 불면증 치료법


# 1. 주어진 숫자 * N
# 2. num의 각 자리 수에 0 ~ 9 까지 숫자가 있는지 확인
# 3. 1-2.를 반복한다.
# 4. 0 ~ 9 까지 숫자가 모두 있으면, 멈춘다.
# 5. 그 때의 N을 출력한다.

def dupli_del_list(strList):
    strList = set(strList)
    strList = list(strList)
    return strList

def sort_list(strList):
    strList = sorted(strList)
    return strList


t = int(input())

# int, string 문자 전역 변수로 선언
iNumInt = None
iNumStr = ""

for i in range(1, t + 1):
    # 현재 입력받은 숫자 리스트
    nowStr = []

    # 입력받는 숫자
    iNumInt = int(input())
    iNumStr = str(iNumInt)

    k = 1

    while len(nowStr)!=10:

        if len(nowStr)==10:
            print("#" + str(i), iNumInt)
            break

        result = iNumInt * k

        for j in list(str(result)):
            nowStr.extend(j)

            # nowStr 중복 제거
            dupli_del_list(nowStr)

            # 오름차순 정렬
            sort_list(nowStr)
            print(i, k, nowStr)

        k = k + 1




