def solution(brown, yellow):
    wh_list = []    # brown과 yellow로 만들 수 있는 w * h 조합
    answer = []
    for i in range(3, int((brown+yellow)**0.5)+1):
        if (brown + yellow) % i == 0:
            w = i
            h = (brown+yellow)//i
            if w < h:
                w, h = h, w     # wh의 0번 index가 무조건 w 값이 되도록
            wh = [w, h]
            wh_list.append(wh)
    for i in wh_list:   # yellow가 무조건 중앙에 오는지 확인
        if brown != ((i[0] * 2) + 2 * (i[1] - 2)) or yellow != ((i[0]-2) * (i[1]-2)):
            continue
        else:
            answer.append(i[0])
            answer.append(i[1])
            break

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))