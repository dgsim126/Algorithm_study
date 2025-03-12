# gpt
def solution(n):
    return bin(n).count('1')

# google
# def solution(n):
#     ans = 1
#     while n != 1:
#         if n % 2 == 0:
#             n /= 2
#         else:
#             n -= 1
#             ans += 1
#     return ans


# def solution(n):
#     b = []
#     ii = [2,3,4,5,6,7,8,9]

#     for i in ii:
#         while n // i != 0:
#             n //= i
#             i *= 2
#         b.append(n)

#     return min(b)