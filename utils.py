from PIL import Image, ImageDraw

CELL_SIZE = 20
WALL_COLOR = (0, 0, 0)
PATH_COLOR = (255, 255, 255)
SOLUTION_COLOR = (255, 0, 0)

def draw_maze(maze):
    rows, cols = len(maze), len(maze[0])
    image = Image.new('RGB', (cols * CELL_SIZE, rows * CELL_SIZE), color=WALL_COLOR)
    draw = ImageDraw.Draw(image)

    for row in range(rows):
        for col in range(cols):
            color = PATH_COLOR if maze[row][col] == ' ' else WALL_COLOR
            x0, y0 = col * CELL_SIZE, row * CELL_SIZE
            x1, y1 = x0 + CELL_SIZE, y0 + CELL_SIZE
            draw.rectangle([x0, y0, x1, y1], fill=color)

    return image

def draw_solution(maze, solution_path):
    image = draw_maze(maze)
    draw = ImageDraw.Draw(image)

    for row, col in solution_path:
        x0, y0 = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
        x1, y1 = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
        draw.line([x0, y0, x1, y1], fill=SOLUTION_COLOR, width=3)

    return image

def save_image(image, filename):
    image.save(filename)
