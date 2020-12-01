import pygame
import json
import random
from pathlib import Path

pygame.init()


class Puzzle:
    puzzle_dir = Path(__file__).parent.parent / 'puzzle_db/'

    display_size = (600, 600)
    background_color = pygame.Color('white')
    line_color = pygame.Color('black')
    selection_color = pygame.Color('blue')

    def __init__(self, puzzle_json=None):
        if puzzle_json is None:
            json_path = random.choice(list(self.puzzle_dir.rglob('*.json')))
            puzzle_json = json.load(json_path.open())

        self.square_width = self.display_size[0] / len(puzzle_json[0])
        self.square_height = self.display_size[1] / len(puzzle_json)
        self.squares = [[Square((x, y), self.square_width,
                         self.square_height, puzzle_json[y][x])
                        for x in range(len(puzzle_json[0]))]
                        for y in range(len(puzzle_json))]
        self.selected = None

        self.display = pygame.display.set_mode(self.display_size)
        pygame.display.set_caption("Sudoku")

    def draw(self, key):
        """
        Draws the Board status on display.
        :param io_status: a dict obj representing inputs
        """
        self.display.fill(self.background_color)

        for n in range(9 + 1):
            start_horizontal = (0, n * self.square_height)
            end_horizontal = (self.display_size[0], n * self.square_height)

            start_vertical = (n * self.square_width, 0)
            end_vertical = (n * self.square_width, self.display_size[1])

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

        # draw text of the squares
        for x in range(len(self.squares[0])):
            for y in range(len(self.squares)):
                self.squares[y][x].draw_text(self.display)

        # Overlay a rectangle on the selected square
        if self.selected:
            selected = self.squares[self.selected[1]][self.selected[0]]
            topleft_vertex = (selected.xy_coord[0] * selected.width,
                              selected.xy_coord[1] * selected.height)
            rect = topleft_vertex + (selected.width, selected.height)
            line_width = 4
            pygame.draw.rect(self.display, self.selection_color,
                             rect, line_width)
            # Draw the temp input if applicable
            if key:
                text = selected.input_text_font.\
                    render(str(key), True, selected.input_text_color)
                text_location = (topleft_vertex[0] + text.get_width() / 2,
                                 topleft_vertex[1] + text.get_height() / 2)
                self.display.blit(text, text_location)

        pygame.display.update()

    def select_square(self, mouse_pos):
        """
        Returns the coordinates of the selected square if any.
        :param mouse_pos: a tuple of ints showing mouse position
        :return: a tuple of ints
        """
        # initialize self.selected first
        self.selected = None

        horizontal, vertical = self.display_size
        xy_coord = (int(mouse_pos[0] // self.square_width),
                    int(mouse_pos[1] // self.square_height))

        if mouse_pos[0] < horizontal and mouse_pos[1] < vertical:
            subject = self.squares[xy_coord[1]][xy_coord[0]]
            if subject.get_init() == 0:
                self.selected = xy_coord

    def place_value(self, value):
        """
        Assigns the value to the selected square.
        :param coord: a tuple of ints representing the square.
        :param value: an int
        """
        if self.selected:
            subject = self.squares[self.selected[1]][self.selected[0]]
            if subject.get_init() == 0:
                subject.input_entered = value
                # initializing self.selected
                self.selected = None


class Square:
    init_text_font = pygame.font.SysFont('arial', 40, bold=True)
    input_text_font = pygame.font.SysFont('arial', 30, italic=True)
    init_text_color = pygame.Color('blue')
    input_text_color = pygame.Color('black')

    def __init__(self,
                 xy_coord: "xy-coordinates by indices",
                 width, height,
                 init_value: int):
        self.xy_coord = xy_coord
        self.width = width
        self.height = height
        self.__init_value = init_value
        self.input_entered = None

    def get_init(self):
        return self.__init_value

    def draw_text(self, display):
        horizontal, vertical = display.get_size()
        topleft_vertex = (self.xy_coord[0] * self.width,
                          self.xy_coord[1] * self.height)

        # Draw the value at the center
        text = None
        if self.__init_value != 0:
            text = self.init_text_font.render(str(self.__init_value), True,
                                              self.init_text_color)
        elif self.__init_value == 0 and self.input_entered is not None:
            text = self.input_text_font.render(str(self.input_entered), True,
                                               self.input_text_color)
        if text:
            text_location = (topleft_vertex[0] +
                             self.width / 2 - text.get_width() / 2,
                             topleft_vertex[1] +
                             self.height / 2 - text.get_height() / 2)
            display.blit(text, text_location)
