# 2029. 몫과 나머지 출력하기

a = input()
a = int(a)

for i in range(1, a + 1):
    i1, i2 = input().split()
    i1 = int(i1)
    i2 = int(i2)

    print("#" + str(i), i1 // i2, i1 % i2)



