import pygame
from param import *
from src.board import *
from src.process import *

pygame.font.init()


def main():
    surface = pygame.display.set_mode(surface_size)
    surface.fill((255, 255, 255))  # white background
    pygame.display.set_caption("Sudoku")
    # solution_button =\
    #     pygame.draw.rect(surface, (255, 255, 255), (150, 600, 100, 50))
    status = {"is_running": True, "key": None}

    while status['is_running']:
        for event in pygame.event.get():
            status = event_response(event, status)

        pygame.display.update()


if __name__ == "__main__":
    main()
