#총 설탕 그램 수
sugar=int(input())

#5,3kg 최소 개수
#안 나눠떨어지면 -1 반환
count=0

while sugar>=0:
    if sugar%5==0:
        count+=(sugar//5)
        print(count)
        break
    sugar-=3
    count+=1
    # elif sugar%5!=0:
    #         count=sugar//5
    #         sugar%=5
    #         if(sugar%3==0):
    #             sugar//=3
    #             count+=sugar
    #             print(count)
    #             break
else:
    print(-1)