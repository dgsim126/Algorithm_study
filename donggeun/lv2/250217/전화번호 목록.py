# 접두어이면 False, 접두어가 아니면 True
def solution(phone_book):
    book = sorted(phone_book)

    for i in range(len(book) - 1):
        current = len(book[i])
        temp = book[i + 1]
        # print(temp[0:current], book[i])
        if (temp[0:current] == book[i]):
            return False

    return True


## main ##
phone_book = ["12", "123", "1235", "567", "88"]
print(solution(phone_book))