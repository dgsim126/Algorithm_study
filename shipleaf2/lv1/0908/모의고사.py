def solution(answers):
    answer = []
    n = len(answers)
    arr1 = []
    arr2 = []
    arr3 = []
    for i in range(len(answers)):
        arr1.append(answers[i] - mark1(n)[i])
        arr2.append(answers[i] - mark2(n)[i])
        arr3.append(answers[i] - mark3(n)[i])
    correct1 = arr1.count(0)
    print(correct1)
    correct2 = arr2.count(0)
    print(correct2)
    correct3 = arr3.count(0)
    print(correct3)
    if correct1 == 0 and correct2 == 0 and correct3 == 0:
        return answer
    answer.append(1)
    print(answer)
    if correct1 > correct2:
        if correct3 > correct1:
            answer.pop()
            answer.append(3)
        elif correct3 == correct1:
            answer.append(3)
    if correct2 > correct1:
        answer.pop()
        answer.append(2)
        if correct3 > correct2:
            answer.pop()
            answer.append(3)
    if correct2 == correct1:
        answer.append(2)
        if correct3 == correct2:
            answer.append(3)
        elif correct3 > correct2:
            answer.pop()
            answer.pop()
            answer.append(3)
    return answer

def mark1(n):
    arr1 = []
    start1 = 1
    for i in range(n):
        arr1.append(start1)
        start1 += 1
        if start1 == 6:
            start1 = 1
    return arr1

def mark2(n):
    arr2 = []
    odd = [1,3,4]
    index = 0
    for i in range(n):
        if i % 2 != 0:
            arr2.append(2)
        else:
            arr2.append(odd[index])
            index += 1
            if index > 2:
                index = 0
    return arr2

def mark3(n):
    arr3 = []
    number = [3,1,2,4,5]
    index = 0
    for i in range(n):
        arr3.append(number[index])
        index += 1
        if index > 4:
            index = 0
    return arr3

# 테스트

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))