# 예제 3-1

#500,100,50,10원 짜리
coin_type=[500,100,50,10]

#거스름돈 n
n=1260

#동전의 개수 count
count =0

for i in coin_type:
    count=int(n/i)
    print(count)
    n%=i

