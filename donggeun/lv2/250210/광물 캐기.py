# 피로도를 최소화하는게 목적
# 어떤 순서로 곡괭이를 사용할지 정해야 하는데.....
# minerals에서 5개씩 끊으면서 값을 구하자! 다이아는 25, 철은 5, 돌은 1!
# 이렇게 5개씩마다의 합이 결정되면 해당 합이 큰 순서대로 정렬
# 정렬된 결과를 다이아 철 톨 곡괭이 순서로 채굴


def solution(picks, minerals):
    temp= len(minerals)
    if(temp%5!=0):
        how= temp%5
        for i in range(5-how):
            minerals.append("nothing")

    print(minerals) # ['diamond', 'diamond', 'diamond', 'iron', 'iron', 'diamond', 'iron', 'stone', 'nothing', 'nothing']

    mine= []
    for i in range(len(minerals)//5):
        mine.append(minerals[i*5:i*5+5])

    print(mine) # [['diamond', 'diamond', 'diamond', 'iron', 'iron'], ['diamond', 'iron', 'stone', 'nothing', 'nothing']]

    # 못 캐는 부분 버리기 # 1차 수정
    sum_= sum(picks)
    print(sum_)
    if(sum_<len(mine)):
        for i in range(len(mine)-sum_):
            mine.pop()

    for i in range(len(mine)):
        result= 0
        for j in range(len(mine[i])):
            if(mine[i][j]=="diamond"): # 2차 수정
                result+=25
            elif(mine[i][j]=="iron"):
                result+=5
            elif(mine[i][j]=="stone"):
                result+=1
        mine[i].append(result)

    print(mine) # [['diamond', 'diamond', 'diamond', 'iron', 'iron', 13], ['diamond', 'iron', 'stone', 'nothing', 'nothing', 6]]

    # mine[i][5]가 큰 순서대로 정렬
    mine.sort(key= lambda x: x[5], reverse=True)
    print(mine)

    # 피로도 계산
    tool= 0
    result= 0

    for i in range(len(mine)):
        current_tool= -1
        if(picks[tool]!=0):
            picks[tool]-=1
            current_tool= tool
        else:
            tool+=1
            if (picks[tool] != 0):
                picks[tool] -= 1
                current_tool = tool
            else:
                tool += 1
                picks[tool] -= 1
                current_tool = tool

        for j in range(5):
            if(current_tool==0):
                if(mine[i][j]!="nothing"):
                    result+=1
            elif(current_tool==1):
                if(mine[i][j]=="diamond"):
                    result+=5
                elif(mine[i][j]!="nothing"):
                    result+=1

            elif(current_tool==2):
                if(mine[i][j]=="diamond"):
                    result+=25
                elif(mine[i][j]=="iron"):
                    result+=5
                elif(mine[i][j]=="stone"):
                    result+=1

    return result


## main ##
picks= [0, 1, 1] # 다이아, 철, 돌
minerals= ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"]
print(solution(picks, minerals))