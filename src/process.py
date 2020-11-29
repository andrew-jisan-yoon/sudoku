import pygame
import sys


def select_puzzle(puzzle_id=None):
    puzzle_dir = Path(__file__).parent.parent / 'puzzle/'
    if puzzle_id:
        json_path = puzzle_dir / f'{puzzle_id}.json'
    else:
        json_path = random.choice(list(puzzle_dir.rglob('*.json')))
    puzzle = json.load(json_path.open())
    assert (len(puzzle) == 9) and (len(puzzle[0]) == 9),\
        "puzzle is not a Sudoku."
    return puzzle


def event_response(board, io_status, event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()

    # ======= Keyboard input ====
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            io_status['key'] = 1
        if event.key == pygame.K_2:
            io_status['key'] = 2
        if event.key == pygame.K_3:
            io_status['key'] = 3
        if event.key == pygame.K_4:
            io_status['key'] = 4
        if event.key == pygame.K_5:
            io_status['key'] = 5
        if event.key == pygame.K_6:
            io_status['key'] = 6
        if event.key == pygame.K_7:
            io_status['key'] = 7
        if event.key == pygame.K_8:
            io_status['key'] = 8
        if event.key == pygame.K_9:
            io_status['key'] = 9

        if event.key == pygame.K_RETURN:
            if io_status['selected']:
                board.place_value(io_status['selected'], io_status['key'])
                io_status['selected'], io_status['key'] = None, None

    # ======= Mouse input =======
    if event.type == pygame.MOUSEBUTTONDOWN:
        # Deselect all squares first
        for i in range(9):
            for j in range(9):
                board.puzzle[i][j].is_selected = False

        mouse_pos = pygame.mouse.get_pos()
        io_status['selected'] = board.select_square(mouse_pos)
        if io_status['selected']:
            io_status['key'] = None  # initializes the key value

    return io_status


def autocomplete():
    """
    Autocompletes the Sudoku puzzle
    """
    pass
