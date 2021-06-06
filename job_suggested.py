
# suggested 1
def solution(a, b, board):
    #print(p1)
    #print(p2)
    #print(board)

    answer = []

    for i in range(8) :

        # 배열의 i 인덱스에 있는 값을 가져와서, int형 으로 변경
        a[i] = int(a[i])
        b[i] = int(b[i])

        # 출력
        #print("a", a[i])
        #print("b", b[i])

        #print(bin(a[i]))
        #print(bin(b[i]))

        # i 인덱스에 있는 값을 or 연산 -> 두 지도를 합친다고 했으므로,
        c  = a[i] | b[i]
        #print(c)

        # 연산 결과 c를 2진수로 변경
        c = bin(c)[2:10]
        #print(c, "2진수로 변경 후")

        # 결과값에서 1 -> *, 0 -> 공백 으로 변경
        c_mod = c.replace("1","*")
        c_mod = c_mod.replace("0", " ")
        #print(c_mod)

        # answer 배열에 값 넣기
        answer.append(c_mod)


    print("정답 : ",answer)




if __name__ == '__main__':
    solution([159, 161, 39, 164, 135, 145, 182, 224],
             [241, 129, 228, 165, 3, 1, 160, 25],
             ['*** ** *', '**   *  ', '* * * **', '*** ** *', '**   *  ', '* * * **', '*** ** *', '**   *  '])


