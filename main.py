from maze import Maze
from solver import MazeSolver
from utils import draw_maze, draw_solution, save_image

def main():
    difficulty = input("Choose difficulty (beginner/intermediate/expert): ").lower()
    maze = Maze(difficulty)
    maze_grid = maze.get_maze()

    # Draw and save the maze
    maze_image = draw_maze(maze_grid)
    save_image(maze_image, 'maze.png')

    # Solve the maze
    solver = MazeSolver(maze_grid)
    solution_path = solver.get_solution_path()

    # Draw and save the solution
    solution_image = draw_solution(maze_grid, solution_path)
    save_image(solution_image, 'maze_solution.png')

if __name__ == "__main__":
    main()
