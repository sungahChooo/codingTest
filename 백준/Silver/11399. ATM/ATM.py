#사람 수 입력
people=int(input())

#각 사람의 소요시간 입력
# timeList=[]
# for i in range(people):
#     time=int(input())
#     timeList.append(time)

timeList=list(map(int,input().split()))

#오름차순 배열
timeList.sort()
# print(timeList)

#소요시간 리스트
timeSumList=[]

sum=0
for i in range(people):
    sum+=timeList[i]
    timeSumList.append(sum)

# print(timeSumList)

#모드 소요시간 합 구하기
finalSum=0
for _ in timeSumList:
    finalSum+=_

print(finalSum)