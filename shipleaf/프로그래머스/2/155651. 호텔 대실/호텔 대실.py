import heapq

def solution(book_time):
    # 1. HH:MM -> 분 단위 변환 & 퇴실 시간에 10분 추가
    book_time = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:]) + 10) for s, e in book_time]
    
    # 2. 시작 시간 기준으로 정렬
    book_time.sort()
    
    # 3. 최소 힙(퇴실 시간을 관리)
    rooms = []
    
    for start, end in book_time:
        # 현재 사용 가능한 방이 있는지 확인 (가장 빨리 끝나는 방과 비교)
        if rooms and rooms[0] <= start:
            heapq.heappop(rooms)  # 기존 방 재사용 가능하므로 제거
        heapq.heappush(rooms, end)  # 새 예약 추가
    
    # 4. 필요한 객실의 최대 개수 반환
    return len(rooms)

# 테스트 실행
print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))  # 3
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))  # 1
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))  # 3
