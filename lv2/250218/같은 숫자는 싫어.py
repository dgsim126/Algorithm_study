def solution(arr):
    answer = []
    for i in arr:
        if not answer or i != answer[-1]:
            answer.append(i)
    return answer