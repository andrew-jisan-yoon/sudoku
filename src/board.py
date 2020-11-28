import pygame
import json
from pathlib import Path
import random


class Board:
    display_size = (600, 600)
    display_color = pygame.Color('white')
    init_text_font = pygame.font.SysFont('arial', 40, bold=True)
    input_text_font = pygame.font.SysFont('arial', 30, italic=True)
    line_color = pygame.Color('black')
    init_text_color = pygame.Color('blue')
    input_text_color = pygame.Color('black')
    selection_color = pygame.Color('blue')

    def __init__(self, puzzle: "list of lists"):
        self.puzzle = None

    def set_puzzle(self, puzzle_id=None):
        puzzle_dir = Path(__file__).parent.parent / 'puzzle/'
        if puzzle_id:
            json_path = puzzle_dir / f'{puzzle_id}.json'
        else:
            json_path = random.choice(list(puzzle_dir.rglob('*.json')))
        puzzle = json.load(json_path.open())
        self.puzzle = [[Square((i, j), puzzle[i][j])
                        for i in range(len(puzzle))]
                       for j in range(len(puzzle[0]))]

    def draw(self, io_status):
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
        for i in range(len(self.puzzle)):
            for j in range(len(self.puzzle[0])):
                self.puzzle[i][j].draw_status(self.display,
                                              io_status,
                                              self.init_text_font,
                                              self.input_text_font,
                                              self.selection_color,
                                              self.init_text_color,
                                              self.input_text_color)

    def select_square(self, mouse_pos):
        horizontal, vertical = self.display.get_size()
        if mouse_pos[0] >= horizontal or mouse_pos[1] >= vertical:
            return None

        square_width, square_height = horizontal / 9, vertical / 9
        coord = (int(mouse_pos[0] // square_width),
                 int(mouse_pos[1] // square_height))
        self.puzzle[coord[1]][coord[0]].is_selected = True
        return coord

    def place_value(self, coord, value):
        selected_square = self.puzzle[coord[1]][coord[0]]
        if selected_square.init_value == 0:
            selected_square.input_value = value
            selected_square.is_selected = False


class Square:
    def __init__(self,
                 coord: "coordinates by indices",
                 init_value: int):
        self.coord = coord
        self.init_value = init_value
        self.input_value = None
        self.is_selected = False

    def draw_status(self, display, io_status,
                    init_text_font, input_text_font,
                    selection_color, init_text_color, input_text_color):
        horizontal, vertical = display.get_size()
        topleft_vertex = (self.coord[0] * horizontal / 9,
                          self.coord[1] * vertical / 9)

        # Draw the value at the center
        text = None
        if self.init_value != 0:
            text = init_text_font.render(str(self.init_value), True,
                                         init_text_color)
        elif self.input_value is not None:
            text = input_text_font.render(str(self.input_value), True,
                                          input_text_color)
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
            pygame.draw.rect(display, selection_color, rect, line_width)
            # Draw the key input if applicable
            if io_status['key']:
                text = input_text_font.render(str(io_status['key']), True,
                                              input_text_color)
                text_location = (topleft_vertex[0] + 2, topleft_vertex[1] + 2)
                display.blit(text, text_location)
