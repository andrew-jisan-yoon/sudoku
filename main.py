import pygame
from param import *
from src.board import *
from src.process import *
import json

pygame.init()


def main():
    display = pygame.display.set_mode(display_size)
    init_text_font = pygame.font.SysFont(font_name, font_size, bold=True)
    input_text_font = pygame.font.SysFont(font_name, font_size, italic=True)
    pygame.display.set_caption("Sudoku")
    puzzle = json.load(open("puzzle/00.json", "r"))

    # Drawing the board
    board = Board(display, puzzle, init_text_font, input_text_font,
                  display_color, line_color, selection_color,
                  init_text_color, input_text_color)

    # Running the game
    status = {"key": None, "selected": None}
    while True:
        for event in pygame.event.get():
            status = event_response(board, status, event)
        board.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
