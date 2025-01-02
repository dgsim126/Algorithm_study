# gpt, google
def solution(arr):
    len_arr = len(arr)
    answer = [0,0] # [0 개수, 1 개수]

    def compress(x,y,len_arr):
        first_value = arr[x][y]
        for i in range(x, x + len_arr):
            for j in range(y, y + len_arr):
                if arr[i][j] != first_value: # 영역 분할
                    len_arr //= 2
                    compress(x, y, len_arr) # 행, 열 그대로 (제2사분면)
                    compress(x, y+len_arr, len_arr) # 행 그대로, 열 증가 (제1사분면)
                    compress(x+len_arr, y, len_arr) # 행 증가, 열 그대로  (제3사분면)
                    compress(x+len_arr, y+len_arr, len_arr) # 행, 열 증가 (제4사분면)

                    return # 분할 후 함수 종료, 값 반환

        if first_value == 0:
            answer[0] += 1
        else:
            answer[1] += 1

    compress(0,0,len_arr)

    return answer