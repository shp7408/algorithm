# 1938. 아주 간단한 계산기

import math

a, b = input().split()
a = int(a)
b = int(b)

print(a + b)
print(a - b)
print(a * b)
print(math.trunc(a / b))