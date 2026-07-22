def solution(n):
    answer = 0
    i=0
    while i<=n:
        if i%2==0:
            answer+=i
        i+=1
    return answer