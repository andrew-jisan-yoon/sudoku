import pygame


class Board:

    def __init__(self,
                 display: "pygame.surface",
                 puzzle: "list of lists",
                 line_color: "RGB tuple"):
        self.display = display
        self.puzzle = puzzle
        self.line_color = line_color
        self.squares = [[Square(self.puzzle[i][j], (i, j))
                        for i in len(self.puzzle)]
                        for j in len(self.puzzle[0])]

    def draw():
        horizontal, vertical = self.display.get_size()
        for n in range(9 + 1):
            start_horizontal = (0, n * vertical / 9)
            end_horizontal = (horizontal, n * vertical / 9)

            start_vertical = (n * horizontal / 9, 0)
            end_vertical = (n * horizontal / 9, vertical)

            if n % 3 == 0:
                line_width = 3  # to distinguish 3x3 subgrids
            else:
                line_width = 1
            # draw horiozntal lines
            pygame.draw.line(self.display, self.line_color,
                             start_horizontal, end_horizontal,
                             line_width)
            # draw vertical lines
            pygame.draw.line(self.display, self.line_color,
                             start_vertical, end_vertical,
                             line_width)
        # show status of the squares
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                self.squares[i][j].draw_status()


class Square:
    def __init__(self,
                 coord: "coordinates by indices",
                 value: int):
        self.coord = coord
        self.value = value
        self.is_selected = False

    def draw_status():
        pass
