# gpt

from itertools import combinations

def solution(orders, course):
    result = []
    
    sorted_orders = [''.join(sorted(order)) for order in orders]
    
    for course_size in course:
        comb_dict = {}
        
        for order in sorted_orders:
            for comb in combinations(order, course_size):
                comb_str = ''.join(comb)
                if comb_str in comb_dict:
                    comb_dict[comb_str] += 1
                else:
                    comb_dict[comb_str] = 1
        
        max_count = 0
        for count in comb_dict.values():
            if count >= 2:
                max_count = max(max_count, count)
        
        for comb, count in comb_dict.items():
            if count == max_count and count >= 2:
                result.append(comb)
    
    return sorted(result)

# 테스트
orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]

print(solution(orders, course))