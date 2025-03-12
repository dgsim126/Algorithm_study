def solution(phone_book):
    answer = True
    phone_book.sort()

    shortest = phone_book[0]
    shortest_len = len(shortest)

    for i in range(1, len(phone_book)):
        if phone_book[i][:shortest_len] == shortest:
            return False

    return answer

# 효율성 테스트 2개 실패
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[j][:len(phone_book[i])] == phone_book[i]:
                return False

    return answer
