def solution(sequence, k):
	r_sequence = list(reversed(sequence))
	for i in range(len(r_sequence)):
		sum = 0
		index = 0
		start = 0
		end = 0
		if r_sequence[i] == k:
			index = len(sequence) -1 - i
			for j in range(i, len(r_sequence)):
				if r_sequence[j] == k:
					index = len(sequence) -1 - j
				else:
					break
			return [index, index]

		elif r_sequence[i] < k:
			sum += r_sequence[i]
			start =  len(sequence) -1 - i
			for j in range(i+1, len(r_sequence)):
				sum += r_sequence[j]
				if sum == k:
					end =  len(sequence) -1 - j
					break
				elif sum > k:
					break
			if sum > k:
				continue
			elif sum == k:
				return [start, end]