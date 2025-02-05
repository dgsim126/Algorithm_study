def solution(book_time):
    book_time_m = []

    for start, end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))

        start_time = start_h * 60 + start_m
        end_time = end_h * 60 + end_m + 10

        book_time_m.append([start_time, end_time])

    book_time_m.sort()

    rooms = []

    for start, end in book_time_m:
        rooms.sort()

        if rooms and rooms[0] <= start:
            rooms[0] = end
        else:
            rooms.append(end)

    return len(rooms)