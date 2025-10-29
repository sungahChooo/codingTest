# n 자연수 개수
# m 더하는 횟수
# k 중복하여 더할 수 있는 횟수
n,m,k=map(int,input().split())
#n개의 자연수 입력
data=list(map(int,input().split()))
#정렬
data.sort()

first_max=data[n-1] #가장 큰 수
second_max=data[n-2] #두번째로 큰 수


count=int(m/(k+1)*k)
final_sum=first_max*count
final_sum+=second_max*(m-count)

#이 방식으로 하면  시간 초과
#while True:
#    for i in range(k):
#        if m == 0:
#            break
#        final_sum+=first_max
#        m-=1
#
#    if m == 0:
#        break
#    final_sum += second_max
#    m-=1

print(final_sum)