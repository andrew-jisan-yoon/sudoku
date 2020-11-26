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
    ((300, 300), coord),
    ((900, 900), None)
])
def test_select_square(board):
    pass


@pytest.mark.parametrize("coord,value,expected", [
    (, ,)
])
def test_place_value(board):
    pass
