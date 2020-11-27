import pytest
from src.board import *
from param import *

pygame.init()


@pytest.fixture
def board():
    """Returns a Board instance"""
    display = pygame.display.set_mode(display_size)
    init_text_font = pygame.font.SysFont(font_name, font_size, bold=True)
    input_text_font = pygame.font.SysFont(font_name, font_size, italic=True)
    board = Board(display, init_text_font, input_text_font,
                  display_color, line_color, selection_color,
                  init_text_color, input_text_color)
    return board


@pytest.mark.parametrize("mouse_pos,expected", [
    ((display_size[0] // 2, display_size[1] // 2), (5, 5)),
    ((display_size[0] * 2, display_size[1] * 2), None)
])
def test_select_square(board, mouse_pos, expected):
    result = board.select_square(mouse_pos)
    assert result == expected


# @pytest.mark.parametrize("coord,value,expected", [
#     ((5, 5), ,)
# ])
def test_place_value(board):
    pass
