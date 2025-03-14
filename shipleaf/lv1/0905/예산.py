# GPT 사용

def solution(d, budget):
    d.sort()
    count = 0
    
    for amount in d:
        if budget >= amount:
            budget -= amount 
            count += 1
        else:
            break
            
    return count
