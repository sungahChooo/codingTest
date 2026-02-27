#1~30 중에 없는 수 출력

students=[]

#출석학생 입력받음
for _ in range(28):
    students.append(int(input()))

students.sort()
# print(students)

allStudents=[]
for i in range(30):
    allStudents.append(i+1)
# print(allStudents)

for i in allStudents:
    if i not in students:
        print(i)
