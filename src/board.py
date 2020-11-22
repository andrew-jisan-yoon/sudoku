import pygame


class Board:

    def __init__(self,
                 display: pygame.Surface,
                 puzzle: "list of lists",
                 font: pygame.font.Font,
                 display_color: "RGB tuple",
                 line_color: "RGB tuple",
                 selection_color: "RGB tuple",
                 init_text_color: "RGB tuple",
                 input_text_color: "RGB tuple"):
        self.display = display
        self.puzzle = puzzle
        self.font = font
        self.display_color = display_color
        self.line_color = line_color
        self.selection_color = selection_color
        self.init_text_clor = init_text_color
        self.input_text_color = input_text_color
        self.squares = [[Square((i, j), self.puzzle[i][j])
                        for i in range(len(self.puzzle))]
                        for j in range(len(self.puzzle[0]))]

    def draw(self):
        horizontal, vertical = self.display.get_size()
        self.display.fill(self.display_color)
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
        for i in range(len(self.squares)):
            for j in range(len(self.squares[0])):
                self.squares[i][j].draw_status(self.display,
                                               self.font,
                                               self.selection_color,
                                               self.text_color)

    def select_square(self, mouse_pos):
        horizontal, vertical = self.display.get_size()
        if mouse_pos[0] >= horizontal or mouse_pos[1] >= vertical:
            return None

        square_width, square_height = horizontal / 9, vertical / 9
        coord = (int(mouse_pos[0] // square_width),
                 int(mouse_pos[1] // square_height))
        self.squares[coord[1]][coord[0]].is_selected = True
        return coord

    def place_value(self, coord, value):
        self.squares[coord[1]][coord[0]].value = value


class Square:
    def __init__(self,
                 coord: "coordinates by indices",
                 value: int):
        self.coord = coord
        self.value = value
        self.is_selected = False

    def draw_status(self, display, font, selection_color, text_color):
        horizontal, vertical = display.get_size()
        topleft_vertex = (self.coord[0] * horizontal / 9,
                          self.coord[1] * vertical / 9)

        # Draw the value at the center
        if self.value != 0:
            text = font.render(str(self.value), True, text_color)
            text_location = (topleft_vertex[0] +
                             horizontal / 9 / 2 - text.get_width() / 2,
                             topleft_vertex[1] +
                             vertical / 9 / 2 - text.get_height() / 2)
            display.blit(text, text_location)

        # Overlay a rectangle if selected
        if self.is_selected:
            rect = topleft_vertex + (horizontal / 9, vertical / 9)
            line_width = 4
            pygame.draw.rect(display, selection_color, rect, line_width)
