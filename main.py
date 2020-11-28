import pygame
from src.board import *
from src.process import *

pygame.init()


def main():
    # Drawing the board
    puzzle = select_puzzle()
    board = Board(puzzle)

    # Running the game
    io_status = {"key": None, "selected": None}
    while True:
        for event in pygame.event.get():
            io_status = event_response(board, io_status, event)
        board.draw(io_status)


if __name__ == "__main__":
    main()
