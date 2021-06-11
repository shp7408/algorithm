# 2050. 알파벳을 숫자로 변환

a = input()

list(a)  # 문자열을 리스트로 바로 변환

numbers = ""

for i in a:
    i2 = ord(i) - 64  # 문자로 된 각 원소를 숫자로 변환
    numbers += (str(i2) + " ")

print(numbers.rstrip())