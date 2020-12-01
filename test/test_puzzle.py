import pytest
from src.puzzle import *

pygame.init()


class TestPuzzle:

    @pytest.mark.parametrize("puzzle_json, mouse_pos, expected", [
        ([[0]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2),
         (0, 0)),
        ([[0]], (Puzzle.display_size[0] * 2, Puzzle.display_size[1] * 2),
         None),
        ([[9]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2),
         None)
    ])
    def test_select_square(self, puzzle_json, mouse_pos, expected):
        puzzle = Puzzle(puzzle_json)
        puzzle.select_square(mouse_pos)
        result = puzzle.selected
        assert result == expected

    @pytest.mark.parametrize("puzzle_json, xy_coord, value, expected", [
         ([[0]], (0, 0), 1, 1),
         ([[1]], (0, 0), 4, None)
    ])
    def test_place_value(self, puzzle_json, xy_coord, value, expected):
        puzzle = Puzzle(puzzle_json)
        puzzle.place_value(xy_coord, value)
        assert puzzle.squares[xy_coord[1]][xy_coord[0]].user_input == expected


class TestSquare:
    pass
