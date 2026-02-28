numList=[]
#10개 입력받음
for i in range(10):
    numList.append(int(input()))

restList=[]
#42로 나눈 나머지를 구한다

for _ in numList:
    restList.append(_%42)
# print(restList)

setList=set(restList)
print(len(setList))