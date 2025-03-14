def solution(rows, columns, queries):
    answer = []
    array = []
    num = 1
    for i in range(rows):
        list = []
        for j in range(columns):
            list.append(num)
            num += 1
        array.append(list)
    for query in queries:
        array = runQueries(query, array)
        answer.append(findMin(query, array))
    return answer

def runQueries(query, array):
    [x1, y1, x2, y2] = query
    for i in range(x2-2, x1-2, -1):
        array[i+1].insert(y2, array[i].pop(y2-1))
    for i in range(x1, x2):
        array[i-1].insert(y1-1, array[i].pop(y1-1))
    return array

def findMin(query, array):
    [x1, y1, x2, y2] = query
    min = 10000
    for i in range(y1-1, y2):
        if array[x1-1][i] < min:
            min = array[x1-1][i]
        if array[x2-1][i] < min:
            min = array[x2-1][i]
    for j in range(x1, x2-1):
        if array[j][y1-1] < min:
            min = array[j][y1-1]
        if array[j][y2-1] < min:
            min = array[j][y2-1]
    return min

# print(solution(6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]))
# print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))