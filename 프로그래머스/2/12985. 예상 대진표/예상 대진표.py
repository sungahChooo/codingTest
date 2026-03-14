import math

def solution(n,a,b):
    answer = 0
    
#     if b-a==1:
#         if a%2==0:
#             answer=2
#         else:
#             answer=1
#     if b-a==2:
#         answer=2
#     if b-a==3:
#         if a%2==0:
#             answer=3
#         else:
#             answer=2
        
#     if b-a>=n//2:
#          answer=math.log2(n)
    while a!=b:
        a=(a+1)//2
        b=(b+1)//2
        answer+=1
    return answer