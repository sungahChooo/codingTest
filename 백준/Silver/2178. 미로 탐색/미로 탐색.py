# n,m 입력받음
N,M=map(int,input().split())
graph=[[0]*(M+1) for _ in range(N+1)] #비워두지말고 0으로 초기화해야함

for x in range(N):
    numbers=list(input())
    # print(numbers)
    for y in range(M):
        graph[x][y]=int(numbers[y])

# print(graph)

dx=[0,0,1,-1]
dy=[1,-1,0,0]

#BFS방식
queue=[(0,0)]
while queue:
    x,y=queue.pop(0)
    for i in range(4):
        next_x,next_y=x+dx[i],y+dy[i]
        if 0<=next_x<N and 0<=next_y<M and graph[next_x][next_y]==1:
           queue.append((next_x,next_y))
           graph[next_x][next_y]=graph[x][y]+1
print(graph[N-1][M-1])

