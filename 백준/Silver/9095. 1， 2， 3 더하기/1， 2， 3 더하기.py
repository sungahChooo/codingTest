#테스트 케이스 개수 입력받음
N=int(input())

numbers=[]
for i in range(N):
    numbers.append(int(input()))

#입력받은 수를 1,2,3의 합으로 표현할 수 있는 가지 수
d=[0]*12
d[1]=1
d[2]=2
d[3]=4
for i in range(4,11):
    d[i]=d[i-1]+d[i-2]+d[i-3]

for num in numbers:
    print(d[num])