T=int(input())

words=[]
for _ in range(T):
    R,S=map(str,input().split())
    R=int(R)
    words.append((R,S))


for R,S in words:
    for s in S:
        print(s*R,end="")
    print()
