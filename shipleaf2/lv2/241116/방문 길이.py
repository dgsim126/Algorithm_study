def solution(dirs):
    list = []
    x = 0
    y = 0
    for i in dirs:
        beforePosition = (x,y)
        if i == 'U' and y < 5:
            y += 1
        elif i == "L" and x > -5:
            x -= 1
        elif i == "R" and x < 5:
            x += 1
        elif i == "D" and y > -5:
            y -= 1
        else:
            continue
        afterPosition = (x,y)
        way = [beforePosition, afterPosition]
        list.append(tuple(sorted(way)))
    
    answer = len(set(list))
    return answer

# 테스트 데이터

print(solution("ULURRDLLU"))
# print(solution("LULLLLLLU"))
# print(solution("UDLR"))
