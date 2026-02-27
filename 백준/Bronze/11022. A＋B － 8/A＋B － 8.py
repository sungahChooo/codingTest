#테스트 케이스 개수
N=int(input())

for _ in range(N):
    A,B=map(int,input().split())
    C=A+B
    print(f"Case #{_+1}: {A} + {B} = {C}")