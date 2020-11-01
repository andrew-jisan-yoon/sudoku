import pygame

surface_size = (800, 800)


def event_response(event, status):
    if event.type == pygame.QUIT:
        status["run"] = False

    # ======= Numbers ====
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_1:
            key = 1
        if event.key == pygame.K_2:
            key = 2
        if event.key == pygame.K_3:
            key = 3
        if event.key == pygame.K_4:
            key = 4
        if event.key == pygame.K_5:
            key = 5
        if event.key == pygame.K_6:
            key = 6
        if event.key == pygame.K_7:
            key = 7
        if event.key == pygame.K_8:
            key = 8
        if event.key == pygame.K_9:
            key = 9

    # ==============


def main():
    surface = pygame.display.set_mode(surface_size)
    pygame.display.set_caption("Sudoku")
    clock = pygame.time.Clock()
    status = {"run": True, "key": None}

    while status['run']:
        for event in pygame.event.get():
            status = event_response(event, status)

        pygame.display.update()


main()
pygame.quit()
