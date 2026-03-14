N=int(input())

numbers=[]
for _ in range(N):
    number=input()
    a,b=number.split(',')
    a,b=int(a),int(b)
    numbers.append((a,b))
    print(a+b)