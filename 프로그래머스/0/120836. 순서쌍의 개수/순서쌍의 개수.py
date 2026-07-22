def solution(n):
    answer = 0
    i=1
    yaksu=[]
    while i<=n:
        if n%i==0:
           yaksu.append(i)
        i+=1
    print(yaksu)
    count=0
    for yak in yaksu:
        count+=1
    # if count%2==0:
    #     answer=count
    # else:
    #     answer=count-1
    answer=count
    return answer