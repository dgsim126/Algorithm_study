# def solution(n):
#     answer = ''
#     binary_num = bin(n)
#     index_list = []
#     for i in range(n, -1, -1):
#         if binary_num[i] == '1':
#             index_list.append(i)
#     n = len(index_list)
#     while n >= 0:
#         if index_list[i]
#     return answer

def solution(n):
    binary_n = bin(n)
    while True:
        n += 1
        if binary_n.count("1") == bin(n).count("1"):
            return n
