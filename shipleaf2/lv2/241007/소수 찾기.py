from itertools import permutations	# combinations는 순서를 고려하지 않고 조합, permutations는 순서 고려 조합

def solution(numbers):
	number_list = []	# 가능한 소수 조합을 담을 리스트

	answer = 0
	for i in range(1, len(numbers)+1):	# 한자리 부터 len(numbers) 자리까지 조합
		for number in permutations(numbers, i):
			number = ''.join(number)	# tuple로 출력되기 때문에 원소를 이어 하나의 문자열로 만들기
			if int(number) % 2 != 0 and int(number) != 3:	# 소수는 2를 제외하면 홀수 + 3 제외
				for i in range(2,int(int(number)**0.5)+1):
					if int(number) % i == 0:
						break
					elif i == int(int(number)**0.5) and int(number) % i != 0:	# i가 끝까지 돌았고 약수가 아닐때 즉, number가 소수일때 append
						number_list.append(int(number))
			elif int(number) == 2 or int(number) == 3:	# 2나 3은 무조건 append
				number_list.append(int(number))
			else:
				continue
	return len(set(number_list))

# print(solution("011"))
# print(solution("17"))
print(solution("123"))