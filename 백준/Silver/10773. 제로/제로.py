N=int(input())

stack=[]

for i in range(N):
    x=int(input())
    if x==0:
        stack.pop()
    else:
        stack.append(x)
sum=0
for num in stack:
    sum+=int(num)

print(sum)