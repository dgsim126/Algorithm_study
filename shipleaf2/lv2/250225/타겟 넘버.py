def solution(numbers, target):
    def dfs(index, total):
        if index == len(numbers):
            return 1 if total == target else 0
        
        return dfs(index + 1, total + numbers[index]) + dfs(index + 1, total - numbers[index])

    return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
print(solution([4, 1, 2, 1], 4))