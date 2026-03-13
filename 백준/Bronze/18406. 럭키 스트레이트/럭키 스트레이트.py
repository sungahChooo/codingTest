N=input()
N_len=len(N)

N=list(N)

left_sum=0
right_sum=0
for i in range(N_len//2):
    left_sum+=int(N[i])
for i in range(N_len//2,N_len,+1):
    right_sum+=int(N[i])

# print(left_sum,right_sum)
if left_sum==right_sum:
    print('LUCKY')
else:
    print('READY')