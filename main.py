import pygame
from src.puzzle import *
from src.process import *

pygame.init()


def main():
    # Initiating the puzzle
    puzzle = Puzzle()

    # Running the game
    key = None
    while True:
        for event in pygame.event.get():
            key = event_response(puzzle, key, event)
        puzzle.draw(key)


if __name__ == "__main__":
    main()
