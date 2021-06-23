# 1933. 간단한 N 의 약수

a = input()
a = int(a)

answer = []

for i in range(1, a + 1):

    if a % i == 0:
        i = str(i)
        answer.append(i)

print(' '.join(answer))
