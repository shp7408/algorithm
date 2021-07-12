# 프로그래머스 / 레벨 1 / 가운데 글자 가져오기

def solution(s):
    answer = ''

    a = int((len(s) - 1) / 2)

    print(type(a))

    print(s[int(len(s) / 2 - 1): int(len(s) / 2 + 2)] if len(s) % 2 == 0
          else s[int(len(s) - 1 / 2)])

