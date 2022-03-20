def swap_elements(list, e1, e2):
    x1, y1, x2, y2 = e1['x'], e1['y'], e2['x'], e2['y']
    list[x1][y1], list[x2][y2] = list[x2][y2], list[x1][y1]
    return list

def check_impossible_state(state):
    if state.board is None:
        return False
    return True

def print_board(board):
    print('%s %s %s' % (board[0][0], board[0][1], board[0][2]))
    print('%s %s %s' % (board[1][0], board[1][1], board[1][2]))
    print('%s %s %s\n' % (board[2][0], board[2][1], board[2][2]))

def print_solution(initial_state, final_state):
    path_to_solution = []
    current_state = final_state
    while current_state.board != initial_state.board:
        path_to_solution.insert(0, current_state.board)
        current_state = current_state.come_from
    path_to_solution.insert(0, initial_state.board)
    for i in range(len(path_to_solution)):
        print('Step #%d:' % (i+1))
        print_board(path_to_solution[i])

