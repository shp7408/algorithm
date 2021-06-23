# 프로그래머스 / 레벨 1 / 포켓몬

def solution(nums):
    numSet = set(nums)
    answer = len(numSet) if len(numSet) < len(nums) / 2 else len(nums) / 2
    return answer