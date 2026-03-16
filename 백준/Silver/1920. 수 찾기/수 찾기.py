N=int(input())
A=set(map(int,input().split()))

M=int(input())
numbers=list(map(int,input().split()))

# print(A)
# print(numbers)

for _ in numbers:
    if _ in A:
        print(1)
    else:
        print(0)