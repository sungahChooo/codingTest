#입력받을 정수 개수
N=int(input())

numList=[]
numList=list(map(int,input().split()))

#찾으려는 수
num=int(input())

count=0

for _ in numList:
    if num == _:
        count+=1

print(count)