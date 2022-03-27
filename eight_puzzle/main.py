from state import State
from helpers import print_solution
from a_star import A_Star
from heuristics import manhattan_distance
from bfs import BFS

initial_state = State([[5, 7, 0], [1, 8, 2], [3, 6, 4]], None)
final_state = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None)

solution_bfs, num_visited_nodes_bfs = BFS(initial_state, final_state)
print(f"Number of visited nodes BFS: {num_visited_nodes_bfs}")

solution, num_visited_nodes = A_Star(initial_state, final_state, manhattan_distance)
print(f"Number of visited nodes A* (Manhattan distance): {num_visited_nodes}")
print_solution(initial_state, solution)
