# 장르 > 재생 > 고유번호(i) 낮은 순서
from collections import deque

def solution(genres, plays):
    result = []
    dic = {}

    for i in range(len(genres)):
        if (genres[i] in dic):
            dic[genres[i]] += plays[i]
        else:
            dic[genres[i]] = plays[i]

    for i in range(len(genres)):
        result.append([i, dic[genres[i]], plays[i]])

    print(result)  # [[0, 3, 500], [1, 2, 600], [2, 3, 150], [3, 3, 800], [4, 2, 2500]]

    # 이제 result에서 1번째가 높은 기준으로, 2번째가 높은 기준으로, 0번째가 낮은 기준으로 정렬하면 된다.
    temp = sorted(result, key=lambda x: (-x[1], -x[2], x[0]))

    print(temp) # [[3, 3, 800], [0, 3, 500], [2, 3, 150], [4, 2, 2500], [1, 2, 600]]

    answer = []
    answer.append(temp[0][0])
    current_genres= temp[0][1]
    current_cnt= 1

    for i in range(1, len(temp)):
        if(temp[i][1]==current_genres):
            if(current_cnt== 1):
                answer.append(temp[i][0])
                current_cnt+=1
            else:
                current_cnt= 0

        else:
            current_genres= temp[i][1]
            current_cnt= 1
            answer.append(temp[i][0])

    return answer




## main ##
genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]
print(solution(genres, plays))