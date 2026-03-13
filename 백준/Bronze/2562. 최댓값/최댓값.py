numbers=[]
for i in range(9):
    numbers.append(int(input()))

# print(numbers)

new_list=numbers.copy()

new_list.sort()
print(new_list[8])

for i in range(9):
    if new_list[8] == numbers[i]:
        print(i+1)