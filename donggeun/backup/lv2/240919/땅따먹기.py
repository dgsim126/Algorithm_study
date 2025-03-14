# gpt's help

def solution(land):
    for i in range(1, len(land)):
        land[i][0] += max(land[i-1][1], land[i-1][2], land[i-1][3])
        land[i][1] += max(land[i-1][0], land[i-1][2], land[i-1][3])
        land[i][2] += max(land[i-1][0], land[i-1][1], land[i-1][3])
        land[i][3] += max(land[i-1][0], land[i-1][1], land[i-1][2])

    # 마지막 행에서의 최대값을 반환한다.
    return max(land[-1])

# 예시 테스트
land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))  # 출력: 16
