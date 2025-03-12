# gpt(dictionary)
def solution(players, callings):
    pdic = {player: i for i, player in enumerate(players)} # dictionary comprehension, enumerate

    for call in callings:
        i = pdic[call]
        pdic[call] -= 1
        pdic[players[i-1]] += 1 # gpt
        
        if i > 0:
            players[i-1], players[i] = players[i], players[i-1]
    
    return players

# def solution(players, callings):
#     for calling in callings:
#         for i in range(len(players)):
#             if i > 0 and players[i] == calling:
#                 players[i-1], players[i] = players[i], players[i-1]

#     return players