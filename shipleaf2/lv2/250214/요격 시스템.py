def solution(targets):
	sorted_targets = sorted(targets, key=lambda x: (x[0], x[1]))
	stack = []
	answer = 0
	for target in sorted_targets:
		if not stack:
			stack.append(target)
		else:
			prev = stack.pop(0)
			if prev[0] == target[0]:
				stack.append([prev[0], prev[1]])
			elif target[1] > prev[1]:
				if prev[1] > target[0]:
					stack.append([target[0], prev[1]])
				else:
					answer += 1
					stack.append(target)
			elif target[1] <= prev[1]:
				if prev[1] > target[0]:
					stack.append([target[0], target[1]])
				else:
					answer += 1
					stack.append(target)
	if stack:
		answer += 1

	return answer



### 1. ------------
###         ------------

### 2. ------------
###    ----------

### 3. -------------------
###             ------