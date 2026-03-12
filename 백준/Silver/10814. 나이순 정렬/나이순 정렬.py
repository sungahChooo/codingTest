# 사람수 입력
N=int(input())

members=[]
for i in range(N):
    age,name=list(map(str,input().split()))
    members.append((int(age),name))

# print(members)

members.sort(key=lambda x:x[0])
for age,name in members:
    print(age,name)
