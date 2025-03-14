'''
나간 지점 빠른 순서(늦게 나간 순서)로 정렬
나간 지점 가장 빠른 지점에 카메라 설치 후 해당되는 값들 모두 제거
들어온 지점 느린 순서(늦게 들어온 순서)로 정렬
들어온 순서 가장 느린 지점에 카메라 설치 후 해당되는 값들 모두 제거

위 두 로직 반복 --> 정렬이 너무 많고, 제거할 때, for문도 문제고, pop(특정 인덱스)도 시간 너무 많이 발생
n * nlon(n) + n * n = 기각



'''
# gpt
def solution(routes):
    # 1. 차량의 진출 지점 기준으로 정렬
    routes.sort(key=lambda x: x[1])

    # 2. 첫 번째 차량의 진출 지점에 카메라 설치
    camera = routes[0][1]
    count = 1

    # 3. 다음 차량들 확인
    for i in range(1, len(routes)):
        if routes[i][0] > camera:  # 현재 카메라로 감시할 수 없는 경우
            count += 1  # 새로운 카메라 설치
            camera = routes[i][1]  # 새로운 카메라 위치 설정

    return count
