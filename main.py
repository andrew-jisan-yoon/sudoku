import pygame
from param import *
from src.board import *
from src.process import *

pygame.font.init()


def main():
    display = pygame.display.set_mode(display_size)
    display.fill(display_color)
    fnt = pygame.font.SysFont(font_name, font_size)
    pygame.display.set_caption("Sudoku")
    status = {"is_running": True, "key": None}

    while status['is_running']:
        for event in pygame.event.get():
            status = event_response(event, status)

        pygame.display.update()


if __name__ == "__main__":
    main()
