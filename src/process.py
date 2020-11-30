import pygame
import sys


def event_response(puzzle, key, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # ======= Keyboard input ====
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            key = 1
        if event.key == pygame.K_2:
            key = 2
        if event.key == pygame.K_3:
            key = 3
        if event.key == pygame.K_4:
            key = 4
        if event.key == pygame.K_5:
            key = 5
        if event.key == pygame.K_6:
            key = 6
        if event.key == pygame.K_7:
            key = 7
        if event.key == pygame.K_8:
            key = 8
        if event.key == pygame.K_9:
            key = 9

        if event.key == pygame.K_RETURN:
            puzzle.place_value(key)
            key = None

    # ======= Mouse input =======
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        puzzle.select_square(mouse_pos)
        if puzzle.selected:
            key = None  # initializes the key value

    return key


def autocomplete():
    """
    Autocompletes the Sudoku puzzle
    """
    pass
