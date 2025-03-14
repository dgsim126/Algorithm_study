"""
부분 수열을 찾고자 함
- 합이 k가 되는 수열을 모두 찾은 후, 가장 길이가 짧은 경우를 반환하면 되나?
- 앞에서부터 하나씩 다 도는 건 시간이 너무 오래 걸리니 뒤에서부터 돌아야 할 듯
- 처음 주어진 수열에서 k보다 작거나 같지만 가장 큰 수를 찾은 후 뒤에서부터 시작
"""

"""
정확성 55.9
시간초과와 실패 같이 발생
실패의 경우는 입출력 예 3과 같은 경우
"""
def solution(sequence, k):
    start_index = -1
    last_index= -1
    temp_sum= 0

    # 수열 안에서 k와 근접한 숫자 위치 찾기
    flag= 0
    for i in range(len(sequence)):
        if(sequence[i]>k):
            start_index= i-1
            flag= 1
            break
    if(flag==0):
        start_index= len(sequence)-1

    print(start_index)

    while(start_index>0):
        for i in range(start_index, 0, -1):
            temp_sum+= sequence[i]
            if(temp_sum==k):
                last_index= i
                # 여기에서 앞에 값도 같은지 확인하며 이동하면 실패는 제거 가능
                return [last_index, start_index]
            elif(temp_sum>k):
                start_index-=1
                temp_sum= 0
                break


def solution(sequence, k):
    start, end = 0, 0
    curr_sum = sequence[0]
    min_length = float('inf')
    result = []

    while end < len(sequence):
        if curr_sum < k:
            end += 1
            if end < len(sequence):
                curr_sum += sequence[end]
        elif curr_sum > k:
            curr_sum -= sequence[start]
            start += 1
        else:  # curr_sum == k
            if (end - start) < min_length:
                min_length = end - start
                result = [start, end]
            start += 1
            if start <= end:
                curr_sum -= sequence[start - 1]

    return result

# 투포인터 최적화
def gpt_solution(sequence, k):
    start, end = 0, 0
    curr_sum = sequence[0]
    min_length = float('inf')
    result = []

    while start < len(sequence):
        # 현재 합이 k보다 작고 end가 범위 안에 있을 때 end를 증가
        while end < len(sequence) and curr_sum < k:
            end += 1
            if end < len(sequence):
                curr_sum += sequence[end]

        # 합이 k와 같다면 결과를 갱신
        if curr_sum == k:
            if (end - start) < min_length:
                min_length = end - start
                result = [start, end]

        # start를 증가하며 부분합을 줄임
        curr_sum -= sequence[start]
        start += 1

    return result




## main ##
sequence = [2, 2, 2, 2, 2]
k = 6
print(solution(sequence, k))