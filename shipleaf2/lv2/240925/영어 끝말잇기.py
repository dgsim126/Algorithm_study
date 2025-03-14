def solution(n, words):
    answer = []
    list_for_dic = list(set(words)) # words list에서 중복 제거
    words_dic = {}  # dic에 추가
    for i in range(len(list_for_dic)):
        words_dic[list_for_dic[i]] = 1  # 각 단어 1로 설정

    i = 1
    m = 2
    loop = 1
    words_dic[words[0]] = words_dic[words[0]] - 1
    while i < len(words):
        if words[i-1][-1] != words[i][0] or words_dic[words[i]] == 0:
            answer.append(m)
            answer.append(loop)
            break
        else:
            words_dic[words[i]] = words_dic[words[i]] - 1
            if m == n:
                m = 1
                i += 1
                loop += 1
            else:
                m += 1
                i += 1
    if answer == []:
        answer.append(0)
        answer.append(0)
    return answer

# print(solution(3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))