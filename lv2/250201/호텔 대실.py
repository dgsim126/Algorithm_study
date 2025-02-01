def solution(book_time):
    room_list = []
    for time in book_time:
        if not room_list:
            start = int(time[0].split(":")[0]) * 60 + int(time[0].split(":")[1])
            end = int(time[1].split(":")[0]) * 60 + int(time[1].split(":")[1]) + 10
            room_list.append([[start, end]])
        else:
            start = int(time[0].split(":")[0]) * 60 + int(time[0].split(":")[1])
            end = int(time[1].split(":")[0]) * 60 + int(time[1].split(":")[1]) + 10
            add_room = True
            for i in range(len(room_list)):
                enable = True
                for disabled in room_list[i]:
                    if start <= disabled < end:
                        enable = False
                        break
                if enable:
                    room_list[i].append([start, end])
                    add_room = False
                    break
            if not add_room:
                room_list.append([start, end])
                print(room_list)

    return len(room_list)                                
                


print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))