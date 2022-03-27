from heapq import heappush, heappop

# Adapted A*
def A_Star(initial_state, final_state, heuristic):
    min_heap = []
    h = heuristic(initial_state.board, final_state.board)
    heappush(min_heap, (h, initial_state))

    num_visited_states = 0
    visited_states = [initial_state.board]
    while len(min_heap) > 0:
        (_, current_state) = heappop(min_heap)
        num_visited_states += 1

        if current_state.board == final_state.board:
            return current_state, num_visited_states

        possible_moves = current_state.generate_moves()
        for next_move in possible_moves:
            if not next_move.board in visited_states:
                visited_states.append(next_move.board)
                h = heuristic(next_move.board, final_state.board)
                heappush(min_heap, (h, next_move))
