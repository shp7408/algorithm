# 2063. 중간값 찾기

a = int(input())

list1 = input().split()

list1 = list(map(int, list1))

list1.sort()

num = a // 2

print(list1[num])