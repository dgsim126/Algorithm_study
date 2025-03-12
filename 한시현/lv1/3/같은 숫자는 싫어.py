def solution(arr):
    answer = []
    for i in arr:
        if i not in answer or answer and i != answer[-1]:
            answer.append(i)
    return answer