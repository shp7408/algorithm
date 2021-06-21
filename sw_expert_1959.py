# 1959. 두 개의 숫자열


# 입력받은 값을 int 형 리스트로 변환
def list_To_int():
    list1 = input().split()
    list1 = list(map(int, list1))
    return list1


def which_Big_List(a, b):
    if len(a) > len(b):
        C = a
        D = b
    else:
        C = b
        D = a
    return C, D


# 메인 메서드 시작
t = int(input())

for i in range(1, t):
    NM = list_To_int()

    A = list_To_int()
    B = list_To_int()

    C, D = which_Big_List(A, B)

    while len(C) != len(D):
        D.insert(0, 0)

    #print("C " , C)
    #print("D ", D)

    sumIntEList = 0
    sumEList=[] # sumIntEList 의 리스트

    for j in range (10) :
        # C, D 리스트의 인덱스가 같은 것 끼리 곱하기 연산
        E = [x * y for x, y in zip(A, B)]

        #print("E ", E)

        # 리스트의 각 값을 모두 더한다.
        sumIntEList = sum(E)
        sumEList.append(sumIntEList)

        #print("sumIntEList ", sumIntEList)
        #print("sumEList ", sumEList)

        # D 리스트에서 마지막 인덱스의 0을 첫 인덱스 자리로 옮기기
        D.insert(0, D.pop())

        #print("D :" , D)

    print("D :", D)

    #sumEList 의 최대값 구하기
    print("#"+ str(i), max(sumEList))








# C, D 리스트의 인덱스가 같은 것끼리 곱하기 연산 한다.
# 결과 리스트의 값을 모두 더한다.
# 마지막 0을 지우고, 인덱스0 에 0을 집어넣는다.


