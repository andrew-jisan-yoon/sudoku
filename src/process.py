import pygame
import sys


def valid(board, value, location):
    """
    Checks if:
        1) the given number overlaps with another in the same row or column
        2) the given number overlaps with another in 3x3 sub-grid
    Parameters:
        location: (x_coord, y_coord)
    """
    idx_col = location[0]
    idx_row = location[1]

    # checks if overlap in the row
    for col in range(sudoku_columns):
        if idx_col == col:
            continue
        if board[idx_row][col] == value:
            return False

    # checks if overlap in the column
    for row in range(sudoku_rows):
        if idx_row == row:
            continue
        if board[row][idx_col] == value:
            return False

    grid_col = idx_col // 3 * 3
    grid_row = idx_row // 3 * 3

    # checks if overlap in 3x3 subgrid
    for row in range(grid_row, grid_row + 3):
        for col in range(grid_col, grid_col + 3):
            if (row, col) == location:
                continue
            if board[row][col] == value:
                return False

    return True


def event_response(board, status, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # ======= Keyboard input ====
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            status['key'] = 1
        if event.key == pygame.K_2:
            status['key'] = 2
        if event.key == pygame.K_3:
            status['key'] = 3
        if event.key == pygame.K_4:
            status['key'] = 4
        if event.key == pygame.K_5:
            status['key'] = 5
        if event.key == pygame.K_6:
            status['key'] = 6
        if event.key == pygame.K_7:
            status['key'] = 7
        if event.key == pygame.K_8:
            status['key'] = 8
        if event.key == pygame.K_9:
            status['key'] = 9

        if event.key == pygame.K_RETURN:
            if not status['selected']:
                pass
            else:
                board.place_value(status['selected'], status['key'])

    # ======= Mouse input =======
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Deselect all squares first
        for i in range(9):
            for j in range(9):
                board.squares[i][j].is_selected = False

        mouse_pos = pygame.mouse.get_pos()
        status['selected'] = board.select_square(mouse_pos)
        if status['selected']:
            status['key'] = None  # initializes the key value

    return status
