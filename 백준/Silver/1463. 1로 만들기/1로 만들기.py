X=int(input())

# while X!=1:
#     if (X-1)%3==0:
#         X=(X-1)/3
#         count+=2
#     if (X-1)%2==0:
#         X=(X-1)/2
#         count+=2
#     if X%3==0:
#         X/=3
#         count+=1
#     if X%2==0:
#         X/=2
#         count+=1
#     else:
#         X-=1
#         count+=1

d=[0]*(X+1)
for i in range(2,X+1):
    d[i]=d[i-1]+1

    if i%2==0:
        d[i]=min(d[i//2]+1,d[i])
    if i%3==0:
        d[i]=min(d[i//3]+1,d[i])

print(d[X])