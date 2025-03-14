from collections import deque

def solution(n, computers):
    if n == 1:
        return 1
    answer = 0
    network = {}
    computer_set = set()
    for i in range(len(computers)):
        computer_set.add(i)
        if i not in network:
            network[i] = deque([])
        for j in range(len(computers[i])):
            if i != j and computers[i][j] == 1:
                network[i].append(j)
    print(network)
    
    start = 0
    computer_set.remove(0)
    # def bfs(start):
        
        
        
        
        
        
        