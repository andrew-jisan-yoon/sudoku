import pytest
from src.process import *


def test_select_puzzle():
    pass


def test_event_response():
    pass


@pytest.mark.parametrize("puzzle_json, expected", [
    ([[1, 0, 0], [2, 0, 7], [0, 6, 0]], [[1, 5, 3], [2, 8, 7], [4, 6, 9]])
])
def test_autocomplete(puzzle_json, expected):
    puzzle = Puzzle(puzzle_json)
    autocomplete(puzzle)
    result = [[puzzle.squares[y][x].input_entered
              for x in range(len(puzzle.squares[0]))]
              for y in range(len(puzzle.squares))]
    assert result == expected


def test_find_empty():
    pass
