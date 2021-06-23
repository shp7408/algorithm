# 1545. 거꾸로 출력해 보아요

a = int(input())
result = []

for i in range(a + 1):
    minus = a - i
    result.append(str(minus))

print(' '.join(result))