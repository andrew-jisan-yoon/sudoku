import pytest
from src.puzzle import *

pygame.init()


class TestPuzzle:

    @pytest.mark.parametrize("puzzle_json, mouse_pos, expected, is_selected", [
        ([[0]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2),
         (0, 0), True),
        ([[0]], (Puzzle.display_size[0] * 2, Puzzle.display_size[1] * 2),
         None, False),
        ([[9]], (Puzzle.display_size[0] // 2, Puzzle.display_size[1] // 2),
         None, False)
    ])
    def test_select_square(self, puzzle_json, mouse_pos,
                           expected, is_selected):
        puzzle = Puzzle(puzzle_json)
        result = puzzle.select_square(mouse_pos)
        assert result == expected
        assert puzzle.squares[0][0].is_selected == is_selected

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
