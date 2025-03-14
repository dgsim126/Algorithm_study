def solution(word):
    # 사전 순서
    vowels = ['A', 'E', 'I', 'O', 'U']

    # 자리별 가중치 계산
    weights = [781, 156, 31, 6, 1]  # 5**4, 5**3, ..., 5**0

    # 순서 계산
    result = 0
    print(f"Word: {word}")
    for i, char in enumerate(word):
        index = vowels.index(char)  # 해당 글자의 순서 (0부터 시작)
        weight = weights[i]  # 해당 자리의 가중치
        contribution = index * weight + 1  # 이 글자의 기여도 계산

        print(f"Position {i + 1} ({char}):")
        print(f"  Index in vowels: {index}")
        print(f"  Weight for position: {weight}")
        print(f"  Contribution to result: {contribution}")

        result += contribution

    print(f"Final result: {result}")
    return result


# 테스트
print(solution("AAAAE"))  # 6
print(solution("AAAE"))  # 10
print(solution("I"))  # 1563
print(solution("EIO"))  # 1189



"""
Word: AAAAE
Position 1 (A):
  Index in vowels: 0
  Weight for position: 781
  Contribution to result: 1
Position 2 (A):
  Index in vowels: 0
  Weight for position: 156
  Contribution to result: 1
Position 3 (A):
  Index in vowels: 0
  Weight for position: 31
  Contribution to result: 1
Position 4 (A):
  Index in vowels: 0
  Weight for position: 6
  Contribution to result: 1
Position 5 (E):
  Index in vowels: 1
  Weight for position: 1
  Contribution to result: 2
Final result: 6
6
"""