# N,M입력받음
# N번박스까지 있고 M번 역순 처리 함
N,M=map(int,input().split())

numList=[]
for _ in range(N):
    numList.append(_+1)
# print(numList)

for _ in range(M):
    i,j=map(int,input().split())
    numList[i-1:j]=numList[i-1:j][::-1]

print(*numList)

