def solution(numbers, direction):
    answer = []
    
    length=len(numbers)
    
    if direction=="right":
        answer.append(numbers[length-1])
        for num in range(0,length-1):
            answer.append(numbers[num])
        
    else:
        for num in range(1,length):
            answer.append(numbers[num])
        answer.append(numbers[0])
    
    return answer