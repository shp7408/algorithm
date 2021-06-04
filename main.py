
# suggested 1
def solution(a, b, board):
    #print(p1)
    #print(p2)
    #print(board)




    # 오름차순으로 정렬해서 연산 해보기
    a.sort()
    a.reverse()
    b.sort()
    #[39, 135, 145, 159, 161, 164, 182, 224]
    #[1, 3, 25, 129, 160, 165, 228, 241]

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


