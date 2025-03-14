def solution(players, callings):
    result = {player: i for i, player in enumerate(players)}

    for who in callings:
        idx = result[who]
        result[who] -= 1
        result[players[idx-1]] += 1
        players[idx-1], players[idx] = players[idx], players[idx-1]  # 위치 변경
    return players


## main ##
players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))
