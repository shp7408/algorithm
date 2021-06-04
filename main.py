
# suggested 1
def solution(a, b, board):
    #print(p1)
    #print(p2)
    #print(board)


    # 리스트 a의 값을 2진수로 바꿔서, a 에 저장하기
    d = int(a[0]) + int(b[0])
    print(bin(d)[2:])

    e = int(a[1]) + int(b[1])
    print(bin(e)[2:])

    f = int(a[2]) + int(b[2])
    print(bin(f)[2:])

    g = int(a[3]) + int(b[3])
    print(bin(g)[2:])

    h = int(a[4]) + int(b[4])
    print(bin(h)[2:])

    i = int(a[5]) + int(b[5])
    print(bin(i)[2:])

    j = int(a[6]) + int(b[6])
    print(bin(j)[2:])

    k = int(a[7]) + int(b[7])
    print(bin(k)[2:])



    print(a)
    print(b)

    c  = bin(int(a[0]))
    d = bin(int(b[0]))


    for x in a:
        print(bin(int(a[0])))




if __name__ == '__main__':
    solution([159, 161, 39, 164, 135, 145, 182, 224],
             [241, 129, 228, 165, 3, 1, 160, 25],
             ['*** ** *', '**   *  ', '* * * **', '*** ** *', '**   *  ', '* * * **', '*** ** *', '**   *  '])


