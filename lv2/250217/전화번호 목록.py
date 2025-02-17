def solution(phone_book):
    sorted_phone = sorted(phone_book)
    for i in range(len(sorted_phone)-1):
        if len(sorted_phone[i]) <= len(sorted_phone[i+1]) and sorted_phone[i] == sorted_phone[i+1][0:len(sorted_phone[i])]:
            return False
    return True


print(solution(["119", "97674223", "1195524421"]))


# def solution(phone_book):
#     phone_book.sort()
#     dic = {}
#     i = 1
#     key = phone_book[0] 
#     dic[key] = []
#     while i < len(phone_book):
#         if len(key) == len(phone_book[i]):
#             i += 1
#             continue
#         elif (len(key) < len(phone_book[i])) and (key[0] == phone_book[i][0]):
#             dic[key].append(phone_book[i])
#             i += 1
#         else:
#             key = phone_book[i]
#             dic[key] = []
#     for i in dic.keys():
#         for values in dic.values():
#             for j in values:
#                 if i[0] == j[0]:
#                     if j == i + j[len(i):]:   # startswith 함수
#                         return False
#     return True