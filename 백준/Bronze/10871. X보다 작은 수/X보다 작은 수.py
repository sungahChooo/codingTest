N,X=map(int,input().split())

numbers=[]
numbers=list(map(int,input().split()))

small_numbers=[]
for _ in numbers:
    if _<X:
        small_numbers.append(_)

new_string=""
for i in small_numbers:

    new_string+=str(i)+" "

print(new_string)
