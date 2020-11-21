import pygame
from param import *
from src.board import *
from src.process import *
import json

pygame.init()


def main():
    display = pygame.display.set_mode(display_size)
    text_font = pygame.font.SysFont(font_name, font_size)
    pygame.display.set_caption("Sudoku")
    puzzle = json.load(open("puzzle/00.json", "r"))

    # Drawing the board
    board = Board(display, puzzle, text_font,
                  display_color, line_color, selection_color, text_color)

    # Running the game
    status = {"key": None, "selected": None}
    while True:
        for event in pygame.event.get():
            status = event_response(board, status, event)
        board.draw()
        pygame.display.update()


if __name__ == "__main__":
    main()
