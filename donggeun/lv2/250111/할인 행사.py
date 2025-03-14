def check(want, number, dict):
    for i in range(len(want)):
        if(want[i] not in dict.keys()):
            return 0
        else:
            if(number[i]>dict[want[i]]):
                return 0
    return 1

def solution(want, number, discount):
    result= 0
    dict= {}

    for i in range(10):
        if discount[i] in dict.keys():
            dict[discount[i]]+=1
        else:
            dict[discount[i]]= 1

    result+= check(want, number, dict)

    for i in range(0, len(discount)-10):
        dict[discount[i]]-=1
        if discount[i+10] in dict.keys():
            dict[discount[i+10]] += 1
        else:
            dict[discount[i+10]] = 1
        result+= check(want, number, dict)

    return result


## main ##
want= ["banana", "apple", "rice", "pork", "pot"]
number= [3, 2, 2, 2, 1]
discount= ["chicken", "apple", "apple", "banana", "rice",
           "apple", "pork", "banana", "pork", "rice",
           "pot", "banana", "apple", "banana"]
print(solution(want, number, discount))