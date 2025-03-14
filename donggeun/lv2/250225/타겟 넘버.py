'''
dfs로 만들 수 있는 모든 경우의 수(부호를 의미)
'''
def solution(numbers, target):

    def dfs(depth, result):
        global cnt

        # 탈출조건
        if(depth>=len_):
            # print(result)
            if(result==target):
                cnt+=1
            return

        add_result= result+numbers[depth]
        dfs(depth+1, add_result)

        minus_result= result-numbers[depth]
        dfs(depth+1, minus_result)



    global cnt
    cnt= 0
    len_= len(numbers)
    dfs(0, 0)

    return cnt
