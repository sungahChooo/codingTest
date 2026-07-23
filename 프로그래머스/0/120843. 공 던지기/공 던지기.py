import math 
def solution(numbers, k):
    answer = 0
    length=len(numbers)
    answer=numbers[(k-1)*2%length]
    return answer