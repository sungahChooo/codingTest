N,M,V=map(int,input().split())


graph=[[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    x,y=map(int,input().split())
    graph[x][y]=graph[y][x] = 1
# print(graph)

visited1=[False]*(N+1)
visited2=[False]*(N+1)

#dfs
def dfs(V):
    visited1[V]=1
    print(V,end=' ')
    for i in range(1,N+1):
        if graph[V][i]==1 and visited1[i]==0:
            dfs(i)

#bfs
def bfs(V):
    queue = [V]
    visited2[V] = 1 #방문처리
    while queue:
        V = queue.pop(0) #방문 노드 제거
        print(V, end = ' ')
        for i in range(1, N+1):
            if(graph[V][i] == 1 and visited2[i] == 0):
                queue.append(i)
                visited2[i] = 1 # 방문처리

dfs(V)
print()
bfs(V)