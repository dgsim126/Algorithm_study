def solution(genres, plays):
    answer = []
    album = {}
    for i in range(len(genres)):
        if genres[i] not in album:
            album[genres[i]] = [plays[i],[[plays[i],i]]]
        else:
            album[genres[i]][0] += plays[i]
            album[genres[i]][1].append([plays[i],i])

    sorted_album = sorted(album.items(),key=lambda item: item[1][0], reverse=True)

    for key, value in sorted_album:
        sorted_value = sorted(value[1], key=lambda x: (-x[0], x[1]))
        print(sorted_value)
        if len(sorted_value) >= 2:
            for i in range(2):
                answer.append(sorted_value[i][1])
        else:
            answer.append(sorted_value[0][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"],[500, 600, 150, 800, 2500]))

## 딕셔너리 정렬