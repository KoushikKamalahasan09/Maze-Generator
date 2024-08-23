from collections import deque

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0])

    def solve(self):
        start = (0, 0)
        end = (self.rows - 1, self.cols - 1)
        queue = deque([start])
        visited = {start: None}

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

        while queue:
            row, col = queue.popleft()

            if (row, col) == end:
                return self._trace_path(visited, end)

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    if self.maze[new_row][new_col] == ' ' and (new_row, new_col) not in visited:
                        queue.append((new_row, new_col))
                        visited[(new_row, new_col)] = (row, col)

        return None  # No solution found

    def _trace_path(self, visited, end):
        path = []
        step = end
        while step is not None:
            path.append(step)
            step = visited[step]
        path.reverse()
        return path

    def get_solution_path(self):
        return self.solve()
