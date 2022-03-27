def manhattan_distance(current_state, final_state):
    distance = 0
    pieces_pos_curr = {}
    pieces_pos_final = {}

    for i, row in enumerate(current_state):
        for j in range(len(row)):
            pieces_pos_curr[current_state[i][j]] = [i, j]
            pieces_pos_final[final_state[i][j]] = [i, j]

    for i in range(len(pieces_pos_curr)):
        distance += abs(pieces_pos_final[i][0] - pieces_pos_curr[i][0]) + abs(
            pieces_pos_final[i][1] - pieces_pos_curr[i][1]
        )

    return distance
