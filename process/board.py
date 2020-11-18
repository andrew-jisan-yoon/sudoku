board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0]
    [6, 0, 0, 1, 9, 5, 0, 0, 0]
    [0, 9, 8, 0, 0, 0, 0, 6, 0]
    [8, 0, 0, 0, 6, 0, 0, 0, 3]
    [4, 0, 0, 8, 0, 3, 0, 0, 1]
    [7, 0, 0, 0, 2, 0, 0, 0, 6]
    [0, 6, 0, 0, 0, 0, 2, 8, 0]
    [0, 0, 0, 4, 1, 9, 0, 0, 5]
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


class Grid:

    def __init__(self, rows, cols, width, height, board, surface):
        self.cubes = [[Cube(board[i][j], i, j, width, height)
                      for j in range(cols) for i in range(rows)]]
        self.surface = surface
        self.selected = None


class Cube:
    def __init__(self, value, row, col, width, height, font):
        self.value = value
        self.selected = False
        self.length = width / 9
        self.font = font

    def draw():
        pass

    def draw_change():
        pass
