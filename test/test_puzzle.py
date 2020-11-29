import pytest
from src.board import *
from param import *

pygame.init()


@pytest.mark.parametrize("puzzle, mouse_pos, expected", [
    ([[0]], (display_size[0] // 2, display_size[1] // 2), (1, 1)),
    ([[0]], (display_size[0] * 2, display_size[1] * 2), None)
])
def test_select_square_with_zero_initial_value(puzzle, mouse_pos, expected):
    result = Board(puzzle).select_square(mouse_pos)
    assert result == expected


@pytest.mark.parametrize("puzzle, mouse_pos, expected", [
    ([[9]], (display_size[0] // 2, display_size[1] // 2), None),
    ([[9]], (display_size[0] * 2, display_size[1] * 2), None)
])
def test_select_square_with_nonzero_initial_value(puzzle, mouse_pos, expected):
    """
    select_square() should return None for squares with nonzero initial values
    """
    pass


@pytest.mark.parametrize("puzzle, coord, value, expected", [
     ([[0]], (1, 1), 1, 1),
     ([[1]], (1, 1), 4, None)
])
def test_place_value(puzzle, coord, value, expected):
    board = Board(puzzle)
    board.place_value(coord, value)
    assert board.puzzle[coord[1]][coord[0]].input_value == expected
