from itertools import permutations

def solution(numbers):
    count = 0
    prime = set()
    for i in range(1, len(numbers)+1):
        for comb in permutations(numbers, i):
            result = int("".join(comb))
            if result <= 1:
                continue
            prime.add(result)
    
    prime = list(prime)
    for i in range(len(prime)):
        is_prime = True
        for j in range(2, int((prime[i])**(1/2))+1):
            if prime[i] % j == 0:
                is_prime = False
                break
        if is_prime:
            count += 1

    return count        

print(solution("011"))