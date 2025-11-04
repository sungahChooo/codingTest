# N,M 차례로 입력, 띄어쓰기로 구분
N, M=map(int,input().split())

count=0
# N이 M의 배수가 될 떄까지 1을 뺀다.
while N%M!=0:
    N-=1
    count+=1

while N!=1:
    N/=M
    count+=1

print(count)