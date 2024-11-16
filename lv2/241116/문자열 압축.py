# def solution(s):
#     answer = 1000
#     rangeNum = len(s)//2
#     for i in range(1, rangeNum+1):
#         word = ""
#         index = 0
#         idxFor = index
#         while len(s) > index:
#             if index + i > len(s):
#                 word = word + s[index:]
#                 break
#             else:
#                 num = 1
#                 term = s[index:index+i]
#                 for k in range(idxFor+i, len(s), i):
#                     index += i
#                     next_term = s[k:k+i]
#                     if term == next_term:
#                         num += 1
#                         if len(s) == index+1:
#                             if num == 1:
#                                 word = word + term
#                             else:
#                                 word = word + str(num) + term
#                             print(word)
#                     else:
#                         if num == 1:
#                             word = word + term
#                         else:
#                             word = word + str(num) + term
#                         print(word)
#                         break

#         if len(word) < answer:
#             answer = len(word)
#     return answer


def solution(s):
    answer = 1000
    rangeNum = len(s) // 2  # 문자열 길이의 절반까지만 반복
    for i in range(1, rangeNum + 1):
        word = ""
        index = 0
        while len(s) > index:
            if index + i > len(s):  # 남은 문자열 처리
                word += s[index:]
                break
            else:
                num = 1
                term = s[index:index+i]  # 현재 단위
                index += i
                while index + i <= len(s) and term == s[index:index+i]:  # 반복되는 단위 계산
                    num += 1
                    index += i
                if num > 1:
                    word += str(num) + term  # 압축된 문자열 추가
                else:
                    word += term  # 반복되지 않으면 그대로 추가
        if len(word) < answer:
            answer = len(word)  # 최소 길이 갱신
    return answer


print(solution("aabbaccc"))