from .imports import *


def drawGrid(screen):
    # creates the gridlines
    for i in range(10):
        if i % 3 == 0:
            pg.draw.line(screen, (0,0,0), (GRID_BOX * i, SCREEN_HEIGHT - BELOW_GRID), (GRID_BOX * i, 0), width=3)
        else:
            pg.draw.line(screen, (0,0,0), (GRID_BOX * i, SCREEN_HEIGHT - BELOW_GRID), (GRID_BOX * i, 0))
    for i in range(10):
        if i % 3 == 0:
            pg.draw.line(screen, (0,0,0), (SCREEN_WIDTH, GRID_BOX * i), (0, GRID_BOX * i), width=3)
        else:
            pg.draw.line(screen, (0,0,0), (SCREEN_WIDTH, GRID_BOX * i), (0, GRID_BOX * i))