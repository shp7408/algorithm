# 2058. 자릿수 더하기

num = str(input())
sum = 0
for i in range(len(num)):
    sum += int(num[i])

print(sum)