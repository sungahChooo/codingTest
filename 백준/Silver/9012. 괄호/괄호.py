#테스트 케이스 입력받음
N=int(input())

for i in range(N):
    parenthesis=[] #선언 위치도 중요함
    str=input()
    for char in str:
        if char=='(':
            parenthesis.append(char)
        elif len(parenthesis)>0 and char==')':
            parenthesis.pop()
        elif len(parenthesis)==0 and char==')':
            print("NO")
            break
    else:
        if len(parenthesis)==0:
            print('YES')
        else:
            print('NO')
    # parenthesis.remove()

