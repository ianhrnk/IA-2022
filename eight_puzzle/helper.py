def swap_elements(list, e1, e2):
    x1, y1, x2, y2 = e1["x"], e1["y"], e2["x"], e2["y"]
    list[x1][y1], list[x2][y2] = list[x2][y2], list[x1][y1]
    return list


def is_impossible_state(state):
    return state.board is not None


def print_board(board):
    print(f"{board[0][0]} {board[0][1]} {board[0][2]}")
    print(f"{board[1][0]} {board[1][1]} {board[1][2]}")
    print(f"{board[2][0]} {board[2][1]} {board[2][2]}\n")


def print_solution(initial_state, final_state):
    path_to_solution = []
    current_state = final_state
    while current_state.board != initial_state.board:
        path_to_solution.insert(0, current_state.board)
        current_state = current_state.previous_state
    path_to_solution.insert(0, initial_state.board)
    for i, board in enumerate(path_to_solution):
        print(f"Step #{i+1}:")
        print_board(board)
