import pygame
import json
import random
from pathlib import Path

pygame.init()


class Puzzle:
    display_size = (600, 600)
    background_color = pygame.Color('white')
    line_color = pygame.Color('black')
    puzzle_dir = Path(__file__).parent.parent / 'puzzle_db/'

    def __init__(self, puzzle_id=None):
        if puzzle_id:
            json_path = puzzle_dir / f'{puzzle_id}.json'
        else:
            json_path = random.choice(list(puzzle_dir.rglob('*.json')))
        puzzle = json.load(json_path.open())

        self.squares = [[Square((i, j), puzzle[i][j])
                        for j in range(len(puzzle[0]))]
                        for i in range(len(puzzle))]
        self.square_width = self.display_size[0] / len(puzzle[0])
        self.square_height = self.display_size[1] / len(puzzle)

        self.display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption("Sudoku")

    def draw(self, io_status):
        """
        Draws the Board status on display.
        :param io_status: a dict obj representing inputs
        """
        self.display.fill(self.background_color)

        for n in range(9 + 1):
            start_horizontal = (0, n * square_height)
            end_horizontal = (horizontal, n * square_height)

            start_vertical = (n * square_width, 0)
            end_vertical = (n * square_width, vertical)

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
        for j in range(len(self.squares[0])):
            for i in range(len(self.squares)):
                self.squares[i][j].draw_status(self.display, io_status)

        pygame.display.update()

    def select_square(self, mouse_pos):
        """
        Returns the coordinates of the selected square if any.
        :param mouse_pos: a tuple of ints showing mouse position
        :return: a tuple of ints
        """
        horizontal, vertical = self.display_size
        if (mouse_pos[0] >= self.display_size[0]) or\
           (mouse_pos[1] >= self.display_size[1]):
            return None

        # formatting the coord into (row_idx, col_idx)
        coord = (int(mouse_pos[1] // square_height),
                 int(mouse_pos[0] // square_width))

        self.puzzle[coord[0]][coord[1]].is_selected = True
        return coord

    def place_value(self, coord, value):
        """
        Assigns the value to the selected square.
        :param coord: a tuple of ints representing the square.
        :param value: an int
        """
        selected_square = self.squares[coord[0]][coord[1]]
        if selected_square.init_value == 0:
            selected_square.input_value = value
            selected_square.is_selected = False


class Square:
    init_text_font = pygame.font.SysFont('arial', 40, bold=True)
    input_text_font = pygame.font.SysFont('arial', 30, italic=True)
    init_text_color = pygame.Color('blue')
    input_text_color = pygame.Color('black')
    selection_color = pygame.Color('blue')

    def __init__(self,
                 coord: "coordinates by indices",
                 init_value: int):
        self.coord = coord
        self.init_value = init_value
        self.input_value = None
        self.is_selected = False

    def draw_status(self, display, io_status):
        horizontal, vertical = display.get_size()
        topleft_vertex = (self.coord[0] * horizontal / 9,
                          self.coord[1] * vertical / 9)

        # Draw the value at the center
        text = None
        if self.init_value != 0:
            text = self.init_text_font.render(str(self.init_value), True,
                                              self.init_text_color)
        elif self.input_value is not None:
            text = self.input_text_font.render(str(self.input_value), True,
                                               self.input_text_color)
        if text:
            text_location = (topleft_vertex[0] +
                             horizontal / 9 / 2 - text.get_width() / 2,
                             topleft_vertex[1] +
                             vertical / 9 / 2 - text.get_height() / 2)
            display.blit(text, text_location)

        # Overlay a rectangle if selected
        if self.init_value == 0 and self.is_selected:
            rect = topleft_vertex + (horizontal / 9, vertical / 9)
            line_width = 4
            pygame.draw.rect(display, self.selection_color, rect, line_width)
            # Draw the key input if applicable
            if io_status['key']:
                text = input_text_font.render(str(io_status['key']), True,
                                              self.input_text_color)
                text_location = (topleft_vertex[0] + 2, topleft_vertex[1] + 2)
                display.blit(text, text_location)