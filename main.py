import pygame
from param import *
from src.board import *
from src.process import *
import json

pygame.init()


def main():
    display = pygame.display.set_mode(display_size)
    display.fill(display_color)
    text_font = pygame.font.SysFont(font_name, font_size)
    pygame.display.set_caption("Sudoku")
    puzzle = json.load(open("puzzle/00.json", "r"))

    board = Board(display, puzzle, text_font,
                  line_color, selection_color, text_color)
    board.draw()
    pygame.display.update()
    # status = {"is_running": True, "key": None}
    # while status['is_running']:
    #     for event in pygame.event.get():
    #         status = event_response(event, status)
    #
    #     pygame.display.update()


if __name__ == "__main__":
    main()
