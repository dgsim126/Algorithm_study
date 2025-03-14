# gpt 실패하는 테스트 케이스 작성해달라고 부탁
# 내가 작성한게 solution 1, gpt solution2
def solution1(cards1, cards2, goal):
    for i in range(len(goal)):
        last= goal.pop()
        if(last==cards1[-1] ):
            cards1.pop()
        elif(last==cards2[-1]):
            cards2.pop()
        else:
            return "No"
    return "Yes"

def solution2(cards1, cards2, goal):
    for word in goal:
        if(len(cards1) > 0 and word == cards1[0]):
            cards1.pop(0)
        elif(len(cards2) > 0 and word == cards2[0]):
            cards2.pop(0)
        else:
            return "No"
    return "Yes"

def solution3(cards1, cards2, goal): # fail 왜 앞에서부터 해야하는가
    for word in goal[::-1]:
        if(len(cards1) > 0 and word == cards1[-1]):
            cards1.pop()
        elif(len(cards2) > 0 and word == cards2[-1]):
            cards2.pop()
        else:
            return "No"
    return "Yes"

## main ##
cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution1(cards1, cards2, goal))

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution2(cards1, cards2, goal))

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]
print(solution3(cards1, cards2, goal))