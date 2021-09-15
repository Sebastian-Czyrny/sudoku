import pygame as pg

pg.init()

smallFont = pg.font.SysFont('bahnschrift', 15)
bigFont= pg.font.SysFont('bahnschrift', 40)

GRID_BOX = 50
BELOW_GRID = 150
SCREEN_WIDTH = 450
SCREEN_HEIGHT = 600

white = 255, 255, 255
black = 0, 0, 0
grey = 225, 225, 225
darkGrey = 50, 50, 50
lightGrey = 240, 240, 240
red = 255, 0, 0
yellow = 255, 234 , 0

numberKeys = [pg.K_1, pg.K_2, pg.K_3, pg.K_4, pg.K_5, pg.K_6, pg.K_7, pg.K_8, pg.K_9]

screen = pg.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

