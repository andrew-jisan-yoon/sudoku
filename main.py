import pygame
from src.puzzle import *
from src.process import *

pygame.init()


def main():
    # Initiating the puzzle
    puzzle = Puzzle()

    # Running the game
    io_status = {"key": None, "selected": None}
    while True:
        for event in pygame.event.get():
            io_status = event_response(puzzle, io_status, event)
        puzzle.draw(io_status)


if __name__ == "__main__":
    main()
