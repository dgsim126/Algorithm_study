# def solution(topping):
# 	answer = 0
# 	topping1 = set()
# 	topping2 = topping
# 	for i in range(len(topping)):
# 		topping1.add(topping2.pop(0))
# 		if len(topping1) == len(set(topping2)):
# 			answer += 1
# 	return answer

def solution(topping):
	answer = 0
	dic_1 = {}
	dic_2 = {}
	num_1 = 0
	num_2 = 0
	for i in range(len(topping)):
		if topping[i] not in dic_2:
			dic_2[topping[i]] = 1
		else:
			dic_2[topping[i]] += 1
			
	num_2 = len(dic_2)
	
	for i in range(len(topping)):
		if topping[i] not in dic_1:
			dic_1[topping[i]] = 1
			dic_2[topping[i]] -= 1
			if dic_2[topping[i]] == 0:
				num_2 -= 1
			num_1 += 1
		else:
			dic_1[topping[i]] += 1
			dic_2[topping[i]] -= 1
			if dic_2[topping[i]] == 0:
				num_2 -= 1
		if num_1 == num_2:
			answer += 1
		
	return answer

print(solution([1, 2, 1, 3, 1, 4, 1, 2]))