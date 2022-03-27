from state import State
from helper import print_solution
from bfs import BFS

initial_state = State([[3, 4, 0], [7, 2, 5], [8, 1, 6]], None)
final_state = State([[1, 2, 3], [4, 5, 6], [7, 8, 0]], None)

solution = BFS(initial_state, final_state)
print_solution(initial_state, solution)
