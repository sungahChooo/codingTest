#주사위 값 3개 입력받음
dice1,dice2,dice3=map(int,input().split())
#print(dice1,dice2,dice3)

#같은 눈의 개수
#3개면 10000 + 1000*같은 눈
#2개면 1000 + 100+같은 눈
#없으면 그 중 가장 큰 눈*100
count=0
sameNum=0

#3개 다 같을 때
if dice1==dice2 and dice1==dice3 and dice2==dice3:
    count+=3

#두개가 같을 때
elif dice1==dice3 and dice1!=dice2:
    count+=2
    sameNum=dice1
elif dice2==dice3 and dice1!=dice2:
    count+=2
    sameNum=dice2
elif dice1==dice2 and dice2!=dice3:
    count+=2
    sameNum=dice1

#다 다를 때
elif dice1!=dice2 and dice1!=dice3 and dice2!=dice3: 
    count+=1

#print(count)
#가장 큰 수
maxNum=max(dice1,dice2,dice3)

if count==3:
    print(10000+1000*dice1)
if count==2:
    print(1000+100*sameNum)
if count==1:
    print(100*maxNum)
