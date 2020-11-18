class Board:

    def __init__(self,
                 display: "pygame.surface",
                 puzzle: "list of lists"):
        self.display = display
        self.puzzle = puzzle
        self.squares = [[Square(self.puzzle[i][j], (i, j))
                        for j in len(self.puzzle)]
                        for i in len(self.puzzle[0])]

    def draw():
        pass


class Square:
    def __init__(self,
                 coord: "coordinates by indices",
                 value: int):
        self.coord = coord
        self.value = value
        self.is_selected = False

    def draw():
        pass
