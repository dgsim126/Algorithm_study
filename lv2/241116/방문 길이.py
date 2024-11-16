def solution(dirs):
    visited_path = set()
    x, y = 0, 0

    for direction in dirs:
        if direction == 'U':
            dx, dy = 0, 1
        elif direction == 'D':
            dx, dy = 0, -1
        elif direction == 'R':
            dx, dy = 1, 0
        else: # direction == 'L'
            dx, dy = -1, 0

        nx = x + dx
        ny = y + dy

        if -5 <= nx <= 5 and -5 <= ny <= 5:
            path = ((x, y), (nx, ny))
            r_path = ((nx, ny), (x, y)) # gpt

            if path not in visited_path and r_path not in visited_path:
                visited_path.add(path)

            x = nx
            y = ny

    return len(visited_path)