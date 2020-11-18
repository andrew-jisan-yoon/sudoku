class Board:

    def __init__(self,
                 window: "pygame.surface",
                 puzzle: "list of lists"):
        self.window = window
        self.puzzle = puzzle
        self.squares = [[Square(self.puzzle[i][j], (i, j))
                        for j in len(self.puzzle)]
                        for i in len(self.puzzle[0])]

    def draw():
        pass


class Square:
    def __init__(self, value, coord):
        self.value = value
        self.coord = coord  # Coordinates by indices
        self.is_selected = False

    def draw():
        pass
