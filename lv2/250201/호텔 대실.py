# def solution(book_time):
#     room_list = []
#     for time in book_time:
#         if not room_list:
#             start = int(time[0].split(":")[0]) * 60 + int(time[0].split(":")[1])
#             end = int(time[1].split(":")[0]) * 60 + int(time[1].split(":")[1]) + 10
#             room_list.append([[start, end]])
#         else:
#             start = int(time[0].split(":")[0]) * 60 + int(time[0].split(":")[1])
#             end = int(time[1].split(":")[0]) * 60 + int(time[1].split(":")[1]) + 10
#             add_room = True     ## 방이 추가로 필요한가
#             for i in range(len(room_list)):     ## 룸 리스트 전체를 돌면서 빈칸을 찾아야 함
#                 enable = True       ## 해당 방에 넣을 수 있는가
#                 for disabled in room_list[i]:       ## 특정 방의 시간을 전부 확인
#                     ## 시간이 겹치는 경우, 두 대실 시간이 같은 경우 체크
#                     if start < disabled[0] < end or start < disabled[1] < end or disabled[0] < start < disabled[1] or disabled[0] < end < disabled[1] or (disabled[1] == end and disabled[0] == start):
#                         enable = False
#                         break
#                 if enable:
#                     room_list[i].append([start, end])
#                     add_room = False
#                     break
#             if add_room:
#                 room_list.append([[start, end]])

#     return len(room_list)

import heapq

def solution(book_time):
    # 시간을 분 단위로 변환하는 함수
    def to_minutes(time):
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes
    
    # 예약 시간을 시작 시간 기준으로 정렬
    book_time.sort(key=lambda x: to_minutes(x[0]))
    
    # 우선순위 큐(최소 힙): 각 방의 퇴실 시간을 관리
    room_heap = []
    
    for start, end in book_time:
        start_time = to_minutes(start)
        end_time = to_minutes(end) + 10  # 청소 시간 10분 추가
        
        # 가장 빨리 퇴실하는 방이 현재 시작 시간보다 먼저 퇴실했으면 재사용 가능
        if room_heap and room_heap[0] <= start_time:
            heapq.heappop(room_heap)  # 퇴실한 방 제거
        
        # 새로운 방 추가
        heapq.heappush(room_heap, end_time)
    
    # 사용된 방의 개수 반환
    return len(room_heap)

# print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
# print(solution([["09:10", "10:10"], ["10:20", "12:20"]])
print(solution([["09:00", "09:30"], ["09:40", "10:10"], ["10:20", "10:50"], ["11:00", "11:30"]]))