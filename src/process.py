import pygame
import sys


def event_response(puzzle, key, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        key = puzzle.select_square(mouse_pos)

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            autocomplete()

        elif event.key == pygame.K_RETURN:
            key = puzzle.place_value(key)

        elif event.key == pygame.K_1:
            key = 1
        elif event.key == pygame.K_2:
            key = 2
        elif event.key == pygame.K_3:
            key = 3
        elif event.key == pygame.K_4:
            key = 4
        elif event.key == pygame.K_5:
            key = 5
        elif event.key == pygame.K_6:
            key = 6
        elif event.key == pygame.K_7:
            key = 7
        elif event.key == pygame.K_8:
            key = 8
        elif event.key == pygame.K_9:
            key = 9

    return key


def autocomplete():
    """
    Autocompletes the Sudoku puzzle
    """
    pass
