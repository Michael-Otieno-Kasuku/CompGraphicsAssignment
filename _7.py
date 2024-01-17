"""
You can generate a simple maze starting with a rectangular array of cells. Each cell has
four sides. You remove sides (except from the perimeter of all the cells) until all the cellsare connected. Then you create an entrance and an exit by removing two sides from the
perimeter.Write a program using PIL for Python that takes as input the two integers N and M and then draws an N * M
maze.
"""

from PIL import Image, ImageDraw
import random

class MazeGenerator:
    def __init__(self, N, M):
        """
        Initialize the MazeGenerator object.

        Parameters:
        - N (int): Number of rows.
        - M (int): Number of columns.

        Returns:
        None
        """
        self.N = N
        self.M = M
        self.maze = [[1 for _ in range(M * 2 + 1)] for _ in range(N * 2 + 1)]
        self.visited = set()

    def generate_maze(self):
        """
        Generate a connected maze using a randomized Prim's algorithm.

        Returns:
        list: The generated maze.
        """
        start_cell = (1, 1)
        self._visit(start_cell)

        # Create entrance and exit
        self.maze[0][1] = 0
        self.maze[self.N * 2][self.M * 2 - 1] = 0

        return self.maze

    def _visit(self, cell):
        """
        Helper method for randomized Prim's algorithm.

        Parameters:
        - cell (tuple): Current cell coordinates.

        Returns:
        None
        """
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
        """
        Draw the generated maze with color.

        Parameters:
        - cell_size (int): Size of each cell in pixels.

        Returns:
        None
        """
        height = len(self.maze)
        width = len(self.maze[0])

        colors = {
            0: "white",  # Path
            1: "black",  # Wall
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
