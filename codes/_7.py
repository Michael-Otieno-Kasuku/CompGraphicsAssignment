from PIL import Image, ImageDraw
import random

class MazeGenerator:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.maze = [[1 for _ in range(M * 2 + 1)] for _ in range(N * 2 + 1)]
        self.visited = set()

    def generate_maze(self):
        start_cell = (1, 1)
        self._visit(start_cell)
        self.maze[0][1] = 0
        self.maze[self.N * 2][self.M * 2 - 1] = 0
        return self.maze

    def _visit(self, cell):
        self.visited.add(cell)
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = cell[0] + dx, cell[1] + dy
            if 0 < nx < self.N * 2 and 0 < ny < self.M * 2 and (nx, ny) not in self.visited:
                self.maze[cell[0] + dx // 2][cell[1] + dy // 2] = 0
                self.maze[nx][ny] = 0
                self._visit((nx, ny))

    def draw_maze(self, cell_size=20):
        height = len(self.maze)
        width = len(self.maze[0])
        colors = {
            0: "white",
            1: "black",
        }
        image = Image.new("RGB", (width * cell_size, height * cell_size), "white")
        draw = ImageDraw.Draw(image)
        for i in range(height):
            for j in range(width):
                color = colors[self.maze[i][j]]
                draw.rectangle(
                    [j * cell_size, i * cell_size, (j + 1) * cell_size, (i + 1) * cell_size],
                    fill=color
                )
        image.show()

if __name__ == "__main__":
    N = int(input("Enter the number of rows (N): "))
    M = int(input("Enter the number of columns (M): "))
    maze_generator = MazeGenerator(N, M)
    maze_generator.generate_maze()
    maze_generator.draw_maze()
