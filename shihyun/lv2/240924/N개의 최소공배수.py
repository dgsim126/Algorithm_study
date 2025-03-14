# gpt
# 유클리드 호제법 : 두 수 a와 b(단, a > b)의 최대공약수는 a를 b로 나눈 나머지 r과 b의 최대공약수와 같다.
# r = 0이라면, a,b의 최대 공약수는 b가 된다.
def gcd(a, b): # 최대공약수 구하는 함수
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b): # 최소공배수를 구하는 함수
    return a * b // gcd(a, b) # 두 수의 곱을 최대공약수로 나누어 최소공배수를 얻는 방식

def solution(arr):
    result = arr[0]
    for num in arr[1:]:
        result = lcm(result, num)
    return result