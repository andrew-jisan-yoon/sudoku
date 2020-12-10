import pytest
from src.process import *
from src.puzzle import *


def test_select_puzzle():
    pass


def test_event_response():
    pass


@pytest.mark.parametrize("puzzle_json, expected", [
    ([[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]],
     [[5, 3, 4, 6, 7, 8, 9, 1, 2],
      [6, 7, 2, 1, 9, 5, 3, 4, 8],
      [1, 9, 8, 3, 4, 2, 5, 6, 7],
      [8, 5, 9, 7, 6, 1, 4, 2, 3],
      [4, 2, 6, 8, 5, 3, 7, 9, 1],
      [7, 1, 3, 9, 2, 4, 8, 5, 6],
      [9, 6, 1, 5, 3, 7, 2, 8, 4],
      [2, 8, 7, 4, 1, 9, 6, 3, 5],
      [3, 4, 5, 2, 8, 6, 1, 7, 9]])
])
def test_autocomplete(puzzle_json, expected):
    puzzle = Puzzle(puzzle_json)
    autocomplete(puzzle)
    result = [[puzzle.squares[y][x].value
              for x in range(len(puzzle.squares[0]))]
              for y in range(len(puzzle.squares))]
    assert result == expected


@pytest.mark.parametrize("puzzle_json, expected", [
    ([[1, 0, 0], [2, 0, 7], [0, 6, 0]],
     [(1, 0), (2, 0), (1, 1), (0, 2), (2, 2)])
])
def test_find_empty(puzzle_json, expected):
    puzzle = Puzzle(puzzle_json)
    result = find_empty(puzzle)
    assert result == expected


@pytest.mark.parametrize("puzzle_json, xy_coord, input, expected", [
    ([[5, 3, 0, 0, 7, 0, 0, 0, 0],
     [6, 0, 0, 1, 9, 5, 0, 0, 0],
     [0, 9, 8, 0, 0, 0, 0, 6, 0],
     [8, 0, 0, 0, 6, 0, 0, 0, 3],
     [4, 0, 0, 8, 0, 3, 0, 0, 1],
     [7, 0, 0, 0, 2, 0, 0, 0, 6],
     [0, 6, 0, 0, 0, 0, 2, 8, 0],
     [0, 0, 0, 4, 1, 9, 0, 0, 5],
     [0, 0, 0, 0, 8, 0, 0, 7, 9]], (4, 4), 5, True),
    ([[5, 3, 0, 0, 7, 0, 0, 0, 0],
      [6, 0, 0, 1, 9, 5, 0, 0, 0],
      [0, 9, 8, 0, 0, 0, 0, 6, 0],
      [8, 0, 0, 0, 6, 0, 0, 0, 3],
      [4, 0, 0, 8, 0, 3, 0, 0, 1],
      [7, 0, 0, 0, 2, 0, 0, 0, 6],
      [0, 6, 0, 0, 0, 0, 2, 8, 0],
      [0, 0, 0, 4, 1, 9, 0, 0, 5],
      [0, 0, 0, 0, 8, 0, 0, 7, 9]], (4, 4), 9, False)
])
def test_is_valid(puzzle_json, xy_coord, input, expected):
    puzzle = Puzzle(puzzle_json)
    result = is_valid(puzzle, xy_coord, input)
    assert result == expected
