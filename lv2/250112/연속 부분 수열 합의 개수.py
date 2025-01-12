# def solution(elements):
#     num_list = []
#     total = 0
#     round_elements = elements * 2
#     for i in range(len(elements)):
#         num_list.append(findNum(round_elements, i))
#     for i in num_list:
#         total += len(i)
#     return total - 1


# def findNum(round_elements, i):
#     number = []
#     for idx in range(len(round_elements)-i):
#         sum = 0
#         for j in range(idx, idx+i):
#             sum += round_elements[j]
#         number.append(sum)
#     return set(number)

# print(solution([7,9,1,1,4]))

def solution(elements):
    # 원형 수열을 만들기 위해 배열을 두 번 연결
    circular_elements = elements * 2
    
    # 모든 부분 수열의 합을 저장할 집합 (중복 제거)
    unique_sums = set()
    n = len(elements)

    # 연속 부분 수열의 길이를 1부터 n까지 반복
    for length in range(1, n + 1):
        # 시작점을 기준으로 연속 부분 수열 계산
        for start in range(n):
            subarray_sum = sum(circular_elements[start:start + length])
            unique_sums.add(subarray_sum)

    # 중복 제거된 합의 개수 반환
    return len(unique_sums)

# 테스트
print(solution([7, 9, 1, 1, 4]))  # 예시 입력