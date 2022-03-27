from copy import deepcopy
from helper import swap_elements, is_impossible_state


class State:
    def __init__(self, board, previous_state):
        self.board = board
        if board is not None:
            self.previous_state = previous_state
            self.pos = self.get_position()

    def get_position(self):
        for row in self.board:
            if 0 in row:
                return {"x": self.board.index(row), "y": row.index(0)}
        return {}

    def generate_moves(self):
        up = State(self.up_move(), self)
        down = State(self.down_move(), self)
        left = State(self.left_move(), self)
        right = State(self.right_move(), self)
        moves = [up, down, left, right]
        return list(filter(is_impossible_state, moves))

    def up_move(self):
        if self.pos["x"] - 1 >= 0:
            num = {"x": self.pos["x"] - 1, "y": self.pos["y"]}
            return swap_elements(deepcopy(self.board), num, self.pos)
        return None

    def down_move(self):
        if self.pos["x"] + 1 <= 2:
            num = {"x": self.pos["x"] + 1, "y": self.pos["y"]}
            return swap_elements(deepcopy(self.board), num, self.pos)
        return None

    def left_move(self):
        if self.pos["y"] - 1 >= 0:
            num = {"x": self.pos["x"], "y": self.pos["y"] - 1}
            return swap_elements(deepcopy(self.board), num, self.pos)
        return None

    def right_move(self):
        if self.pos["y"] + 1 <= 2:
            num = {"x": self.pos["x"], "y": self.pos["y"] + 1}
            return swap_elements(deepcopy(self.board), num, self.pos)
        return None
