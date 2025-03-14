# 83.3

def solution(phone_book):
    phone_book.sort()
    print(phone_book)
    dic = {}
    i = 1
    key = phone_book[0]
    dic[key] = []
    while i < len(phone_book):
        if len(key) == len(phone_book[i]):
            i += 1
            continue
        elif (len(key) < len(phone_book[i])) and (key[0] == phone_book[i][0]):
            dic[key].append(phone_book[i])
            i += 1
        else:
            key = phone_book[i]
            dic[key] = []
    print(dic)
    for i in dic.keys():
        for values in dic.values():
            for j in values:
                if i[0] == j[0]:
                    if j == i + j[len(i):]:   # startswith 함수
                        return False
    return True

print(solution(["12","123","1235","567","88"]))
print(solution(["123","456","789"]))
print(solution(["119", "97674223", "1195524421"]))
