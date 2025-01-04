# f(x) = x보다 크면서 x의 비트와 다른게 1,2개인 가장 작은 수
def solution(numbers):
    answer = []
    for num in numbers:
        next_num = num+1
        while True:
            diff = bin(num ^ next_num).count('1') 비트가 같으면 1, 다르면 0 반환 (같은 비트의 수(1) 세기)
            if diff <= 2: # 다른 비트가 2개 이하라면
                answer.append(next_num) # append 후 for 문 종료 (어차피 순차적이므로 가장 작음)
                break
            next_num += 1

    return answer