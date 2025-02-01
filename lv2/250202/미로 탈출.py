def solution(maps):
    answer = 0
    sx, sy = findStart(maps)
    print(sx, sy)
    point, time = BFSSToL(maps, sx, sy)
    answer += time
    answer += BFSLToE(point, maps)
    return answer
    

def findStart(maps):
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == "S":
                return i, j

def BFSSToL(maps, x, y):
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    loc = [[x, y]]
    visited = set()
    time = 0

    while True:
        
        

def BFSLToE(point, time):
    


print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))