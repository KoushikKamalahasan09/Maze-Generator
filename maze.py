import random
from config import MAZE_CONFIG

class Maze:
    def __init__(self, difficulty):
        self.rows, self.cols = MAZE_CONFIG[difficulty]
        self.grid = [['#' for _ in range(self.cols)] for _ in range(self.rows)]
        self._generate_maze(0, 0)

    def _generate_maze(self, start_row, start_col):
        stack = [(start_row, start_col)]
        self.grid[start_row][start_col] = ' '  # Start position

        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]  # Up, Down, Left, Right

        while stack:
            row, col = stack[-1]
            random.shuffle(directions)

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols and self.grid[new_row][new_col] == '#':
                    self.grid[new_row][new_col] = ' '  # Carve path
                    self.grid[row + dr // 2][col + dc // 2] = ' '  # Remove wall
                    stack.append((new_row, new_col))
                    break
            else:
                stack.pop()

    def get_maze(self):
        return self.grid
