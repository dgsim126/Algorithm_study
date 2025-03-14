def solution(phone_book):
    phone_book= sorted(phone_book)
    # print(phone_book) # ['12', '123', '1235', '567', '88']

    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i + 1][:len(phone_book[i])]:
            return False
    return True


## main ##
phone_book= ["12","123","1235","567","88"]
print(solution(phone_book))