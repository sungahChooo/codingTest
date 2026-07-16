def solution(numer1, denom1, numer2, denom2):
    answer = []
    if denom1==denom2:
        #num1: 분자,num2: 분모
        num1=numer1+numer2
        num2=denom1
    else:
        num1=denom1*numer2+numer1*denom2
        num2=denom1*denom2
    
    #약분
    for i in range(min(num1,num2),1,-1):
            # print(i)
            if num1%i==0 and num2%i==0:
                num1//=i
                num2//=i
        
    answer.append(num1)
    answer.append(num2)             
        
    return answer