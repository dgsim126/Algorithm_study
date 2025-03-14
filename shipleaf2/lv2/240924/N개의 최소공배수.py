# def Factors(n):
#     factors = []
#     def findPrimeFactors(n):
#         factor1 = 0
#         for i in range(2, int(n ** 0.5) + 1):
#             if n % i == 0:
#                 factor1 = i
#         if factor1 == 0:
#             factors.append(n)
#             return
#         else:
#             factor2 = n // factor1
#         number = 0
#         for i in range(2, int(factor1 ** 0.5) + 1):
#             if factor1 % i == 0:
#                 number = i
#         if number == 0:
#             factors.append(factor1)
#             factors.append(factor2)
#             return
#         else:
#             findPrimeFactors(factor1)
#             findPrimeFactors(factor2)
#     return factors

# print(Factors(168))

# def solution(arr):
#     answer = 0
#     dic = {}
#     list = []
#     for i in range(len(arr)):
#         list.append(Factors(arr[i]))
#     for i in range(len(list)):
#         for j in range(len(list[i])):
#             dic[list[i][j]].append(dic[list][i].count(list[i][j]))

#     return answer

def solution(arr):
    dic = {}
    
    # 각 숫자의 소인수 분해 결과 저장
    for i in range(len(arr)):
        factor_list = Factors(arr[i])
        factor_count = {}
        
        # 소인수의 개수를 셈
        for factor in factor_list:
            if factor in factor_count:
                factor_count[factor] += 1
            else:
                factor_count[factor] = 1
        
        # 딕셔너리 업데이트: 최대 개수 유지
        for key, value in factor_count.items():
            if key in dic:
                dic[key] = max(dic[key], value)
            else:
                dic[key] = value
    
    # 최소공배수 계산
    lcm = 1
    for key, value in dic.items():
        lcm *= key ** value
    
    return lcm


def Factors(n):
    factors = []
    
    def findPrimeFactors(n):
        # 2로 계속 나누기
        while n % 2 == 0:
            factors.append(2)
            n //= 2
        
        # 3 이상의 홀수로 나누기
        for i in range(3, int(n ** 0.5) + 1, 2):
            while n % i == 0:
                factors.append(i)
                n //= i
        
        # 만약 n이 2 이상의 소수라면 추가
        if n > 2:
            factors.append(n)
    
    findPrimeFactors(n)
    return factors

print(solution([2,6,8,14]))
