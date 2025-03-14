# 맨 끝 부터 시작해서 위로 한 칸 올리고 만약 범위 포함 안되면 왼쪽으로 한 칸씩 이동
def count(x_index, k):
    # print((x_index//k) + 1)
    return (x_index//k) + 1

def check(y_index, x_index):
    return (y_index**2 + x_index**2)

def my_solution(k, d):
    y_index= 0
    x_index= d
    result= 0
    d_2= d**2

    while(x_index>=0):
        if(check(y_index, x_index)<=d_2):
            # print(f"x_index={x_index}, y_index={y_index}")
            result+= count(x_index, k)
            y_index+=k
        else:
            x_index-=k

    return result

def gpt_solution(k, d):
    result = 0
    d_squared = d ** 2  # 거리의 제곱 계산

    # y_index를 k 간격으로 증가시키며 가능한 x 값 계산
    for y_index in range(0, d + 1, k):
        max_x_index = int((d_squared - y_index ** 2) ** 0.5)  # 최대 x_index 계산
        result += count(max_x_index, k)  # 가능한 x 값 개수 추가

    return result

## main ##
k= 2
d= 4
print(gpt_solution(k, d))