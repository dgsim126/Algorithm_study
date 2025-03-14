# GPT

def solution(numbers):
    # numbers 배열을 문자열로 변환하고, key=lambda x: x*3을 사용하여 정렬
    numbers = sorted(map(str, numbers), key=lambda x: x*3, reverse=True)
    
    # 정렬된 숫자를 이어 붙인 후 반환
    answer = ''.join(numbers)
    
    # '0000' 같은 경우를 방지하기 위해 int로 변환 후 다시 문자열로 변환
    return str(int(answer))


print(solution([6, 10, 2]))  # 출력: "6210"
