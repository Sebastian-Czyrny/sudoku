from .imports import *

def textDisp(screen, str, color, x, y, textSize, colorRect=white, colorRectEx=False):
    font = pg.font.SysFont('bahnschrift', textSize)
    if colorRectEx:
        text = font.render(str , True , color, colorRect)
    else:
        text = font.render(str , True , color)
    textRect = text.get_rect()

    textRect.center = (x, y)
    screen.blit(text, textRect)


def textDisp2(screen, str, color, x, y, textSize, colorRect=white, colorRectEx=False):
    font = pg.font.SysFont('bahnschrift', textSize)
    if colorRectEx:
        text = font.render(str , True , color, colorRect)
    else:
        text = font.render(str , True , color)
    textRect = text.get_rect()

    textRect.right = x
    textRect.bottom = y
    screen.blit(text, textRect)



def failDisp(screen, inputBoxes):
    fails = 0
    for row in inputBoxes:
        for box in row:
            fails += box.fails
    failText = "FAILS: " + str(fails)
    pg.draw.rect(screen, white, pg.Rect(SCREEN_WIDTH/4 - 65, SCREEN_HEIGHT - 145, 130, 50))
    textDisp(screen, failText, black, SCREEN_WIDTH/4, SCREEN_HEIGHT - 120, 30, colorRectEx=True)