from queue import Queue

# Adapted breadth-first-search
def BFS(initial_state, final_state):
    queue = Queue()
    num_visited_states = 0
    visited_states = [initial_state.board]
    queue.put(initial_state)

    while not queue.empty():
        current_state = queue.get()
        print(num_visited_states := num_visited_states + 1)

        if current_state.board == final_state.board:
            return current_state

        possible_moves = current_state.generate_moves()
        for next_move in possible_moves:
            if not next_move.board in visited_states:
                visited_states.append(next_move.board)
                queue.put(next_move)
