# 시간 초과
def solution(sequence, k):
    len_s = len(sequence)
    min_length = len_s + 1
    result = [0, 0]

    for i in range(len_s):
        current_sum = 0
        for j in range(i, len_s):
            current_sum += sequence[j]

            if current_sum == k:
                length = j - i
                if length < min_length:
                    min_length = length
                    result = [i, j]
                break

    return result

def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    len_s = len(sequence)
    min_length = len_s + 1
    result = [0, 0]

    while right < len_s:
        if current_sum < k:
            right += 1
            if right < len_s:
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else:
            if right - left < min_length:
                min_length = right - left
                result = [left, right]
            left += 1
            if left <= right:
                current_sum -= sequence[left - 1]

    return result

# gpt, 정답
def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    len_s = len(sequence)
    min_length = len_s + 1  # 최댓값으로 설정
    result = [-1, -1]  # 기본값 (찾지 못했을 경우)

    while right < len_s:
        if current_sum < k:
            right += 1
            if right < len_s:
                current_sum += sequence[right]
        elif current_sum > k:
            current_sum -= sequence[left]
            left += 1
        else:  # current_sum == k
            length = right - left
            if length < min_length:
                min_length = length
                result = [left, right]
            elif length == min_length and left < result[0]:  # 길이가 같으면 앞쪽 인덱스를 우선
                result = [left, right]

            current_sum -= sequence[left]  # 다음 부분 수열을 확인하기 위해 left 증가
            left += 1

    return result
