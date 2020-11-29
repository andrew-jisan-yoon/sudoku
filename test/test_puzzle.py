import pytest
from src.puzzle import *

pygame.init()


@pytest.mark.parametrize("puzzle_json, mouse_pos, expected", [
    ([[0]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2),
     (1, 1)),
    ([[0]], (Puzzle.display_size[0] * 2, Puzzle.display_size[1] * 2),
     None)
])
def test_Puzzle_select_square_with_zero_initial_value(puzzle_json, mouse_pos,
                                                      expected):
    result = Puzzle(puzzle_json).select_square(mouse_pos)
    assert result == expected


@pytest.mark.parametrize("puzzle_json, mouse_pos, expected", [
    ([[9]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2), None),
    ([[9]], (Puzzle.display_size[0] * 2, Puzzledisplay_size[1] * 2), None)
])
def test_Puzzle_select_square_with_nonzero_initial_value(puzzle_json,
                                                         mouse_pos, expected):
    """
    select_square() should return None for squares with nonzero initial values
    """
    pass


@pytest.mark.parametrize("puzzle_json, coord, value, expected", [
     ([[0]], (1, 1), 1, 1),
     ([[1]], (1, 1), 4, None)
])
def test_Puzzle_place_value(puzzle_json, xy_coord, value, expected):
    puzzle = Puzzle(puzzle_json)
    puzzle.place_value(xy_coord, value)
    assert puzzle.squares[xy_coord[1]][xy_coord[0]].user_input == expected
