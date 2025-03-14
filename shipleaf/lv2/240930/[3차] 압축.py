# def solution(msg):
#     answer = []
#     word_dic = {
#         "A" : 1,
#         "B" : 2,
#         "C" : 3,
#         "D" : 4,
#         "E" : 5,
#         "F" : 6,
#         "G" : 7,
#         "H" : 8,
#         "I" : 9,
#         "J" : 10,
#         "K" : 11,
#         "L" : 12,
#         "M" : 13,
#         "N" : 14,
#         "O" : 15,
#         "P" : 16,
#         "Q" : 17,
#         "R" : 18,
#         "S" : 19,
#         "T" : 20,
#         "U" : 21,
#         "V" : 22,
#         "W" : 23,
#         "X" : 24,
#         "Y" : 25,
#         "Z" : 26
#     }
#     index = 27
#     current_num = 0
#     for i in range(len(msg)):
#         answer.append(word_dic[msg[i]])
#         for j in range(i+1,len(msg)):
#             if (msg[i]+msg[j]) not in word_dic:
#                 word_dic[msg[i]+msg[j]] = index
#                 index += 1
#             else:
#                 answer.append(word_dic[msg[i]+msg[j]])
#                 m = msg[i]+msg[j]
#                 key = j+1
#                 while True:
#                     m = m + msg[index]
#                     if m in word_dic:
#                         answer.append(word_dic[m])
#                         key += 1
#                     else:
#                         word_dic[m] = index
#                         index += 1
#                         break
#     return answer


def solution(msg):
    answer = []
    word_dic = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 6,
        "G" : 7,
        "H" : 8,
        "I" : 9,
        "J" : 10,
        "K" : 11,
        "L" : 12,
        "M" : 13,
        "N" : 14,
        "O" : 15,
        "P" : 16,
        "Q" : 17,
        "R" : 18,
        "S" : 19,
        "T" : 20,
        "U" : 21,
        "V" : 22,
        "W" : 23,
        "X" : 24,
        "Y" : 25,
        "Z" : 26
    }
    index = 27
    cn = 0
    while cn < len(msg):
        if (msg[cn]+msg[cn+1]) not in word_dic: # KA 경우
            word_dic[msg[cn]+msg[cn+1]] = index
            index += 1
            cn += 1
        else:   # 2번째 KA 경우
            m = msg[cn] + msg[cn+1]
            i = cn+2
            while m in word_dic:
                i += 1
                m = m + msg[i]
            word_dic[m] = index
            index += 1
            cn = i
            answer.append(word_dic[m])               
    return answer

print(solution("KAKAO"))