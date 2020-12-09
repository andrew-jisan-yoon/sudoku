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
    empty_squares = find_empty()
    i = 0
    while i != len(empty_squares):
        xy_coord = empty_squares[i]
        for num in range(1, 10):
            if is_valid(puzzle, xy_coord, num):
                puzzle.place_value(xy_coord, num)
                i += 1
        if num == 9 and puzzle.squares[xy_coord[1]][xy_coord[0]].value == 0:
            i -= 1


def find_empty(puzzle):
    """
    Find empty squares in the given board
    """
    empty_squares = []
    for y in range(len(puzzle.squares)):
        for x in range(len(puzzle.squares[0])):
            if puzzle.squares[y][x].is_editable is True:
                empty_squares.append((x, y))
    return empty_squares


def is_valid(puzzle, xy_coord, input):
    """
    Checks if the given input is valid in the given board
    """
    # validate row consistency
    for x in range(len(puzzle.squares[0])):
        if puzzle.squares[xy_coord[1]][x].value == input and xy_coord[0] != x:
            return False

    # validate column consistency
    for y in range(len(puzzle.squares)):
        if puzzle.squares[y][xy_coord[0]].value == input and xy_coord[1] != y:
            return False

    # validate 3x3 subgrid consistency
    x_grid = xy_coord[0] // 3
    y_grid = xy_coord[1] // 3
    for y in range(y_grid * 3, y_grid * 3 + 3):
        for x in range(x_grid * 3, x_grid * 3 + 3):
            if puzzle.squares[y][x].value == input and (x, y) != xy_coord:
                return False

    return True
