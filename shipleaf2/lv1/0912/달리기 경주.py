def solution(players, callings):
    answer = []
    for i in range(len(callings)):
        index = 0
        for j in range(len(players)):
            if players[j] == callings[i]:
                index = j
                break
        players.pop(index)
        player = callings[i]
        players.insert(index-1, callings[i])
    answer = players
    return answer

def solution(players, callings):
    player_indices = {player: i for i, player in enumerate(players)}

    for calling in callings:
        current_index = player_indices[calling]

        if current_index > 0:

            previous_player = players[current_index - 1]
            players[current_index - 1], players[current_index] = players[current_index], players[current_index - 1]

            player_indices[calling] -= 1
            player_indices[previous_player] += 1

    return players
