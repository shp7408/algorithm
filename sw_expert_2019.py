# 2019. 더블더블

a = int(input())
answer = 1
result = []

for i in range(1, a + 2):
    # print(answer)
    result.append(str(answer)) # str 타입으로 변경하는 이유? string 타입의 리스트만 join 사용 가능함

    # 다음 answer 연산
    answer = answer * 2

# 리스트를 공백으로 출력하는 방법이 두 가지가 있는데,
# 1. 반복문으로 리스트 전체 길이만큼 출력
# 2. 기존 리스트의 원소를 str로 변경해서, join 사용하여 출력
print(' '.join(result))