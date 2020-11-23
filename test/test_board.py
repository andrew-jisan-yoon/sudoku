import pytest
from src.board import *
from param import *


@pytest.fixture
def board():
    """Returns a Board instance"""
    display = pygame.display.set_mode(display_size)
    board = Board(display, init_text_font, input_text_font,
                  display_color, line_color, selection_color,
                  init_text_color, input_text_color)
    return board


def test_setting_class_attr(board):
    pass


def test_draw(board):
    pass
