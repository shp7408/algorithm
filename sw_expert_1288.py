# 1288. 새로운 불면증 치료법

# 문제보고, 기겁해서, 바로 못 풀고 넘어갔다.
# 그러다 보니, 이건 알고리즘이 필요한 문제가 아닐까 생각하며
# 합리화하고, 넘겼다.

# 그 다음 날, 다시 찬찬히 문제 보며 정리했다.
# 갈피가 조금 잡힌 듯 하다.

# 1. 주어진 숫자 * N
# 2. num의 각 자리 수에 0 ~ 9 까지 숫자가 있는지 확인
# 3. 1-2.를 반복한다.
# 4. 0 ~ 9 까지 숫자가 모두 있으면, 멈춘다.
# 5. 그 때의 N을 출력한다.


t = int(input())

numList = []

for numInt in range(10):
    numList.append(str(numInt))

# print(numList)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(1, t + 1):
    # 입력받는 숫자
    iNumInt = int(input())
    iNumStr = str(iNumInt)
    for j in iNumStr:
        for k in numList:
            if k == j:
                print("k == j")
            else:
                print("else")
                break
        print(" === ")


