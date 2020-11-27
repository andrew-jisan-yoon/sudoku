import pygame
from param import *
from src.board import *
from src.process import *

pygame.init()


def main():
    display = pygame.display.set_mode(display_size)
    init_text_font = pygame.font.SysFont(font_name, font_size, bold=True)
    input_text_font = pygame.font.SysFont(font_name, font_size, italic=True)
    pygame.display.set_caption("Sudoku")

    puzzle = set_puzzle()

    # Drawing the board
    board = Board(display, puzzle,
                  init_text_font, input_text_font,
                  display_color, line_color, selection_color,
                  init_text_color, input_text_color)

    # Running the game
    io_status = {"key": None, "selected": None}
    while True:
        for event in pygame.event.get():
            status = event_response(board, io_status, event)
        board.draw(io_status)
        pygame.display.update()


if __name__ == "__main__":
    main()
