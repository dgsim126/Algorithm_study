def solution(board, moves):
    n = len(board)
    bag = []
    pang = 0
    for loc in moves:
        ext = 0
        for i in range(n):
            if board[i][loc-1] != 0:
                ext = board[i][loc-1]
                board[i][loc-1] = 0
                break
        if ext != 0:
            bag.append(ext)
        if len(bag) > 1 and bag[-1] == bag[-2]:
            bag = bag[:-2]
            pang += 2
            
    return pang