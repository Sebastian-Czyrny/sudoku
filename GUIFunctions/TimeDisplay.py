from  .imports import *
from . import TextDisplays

## print time in seconds (from milliseconds)
def timeDisplay(timeElapsed, screen):
    timeSec = int(timeElapsed/1000)

    timeMin = 0
    while timeSec > 60:
        timeSec -= 60
        timeMin += 1

    if timeSec < 10:
        timeText = str(timeMin) + ":0" + str(timeSec)
    else:
        timeText = str(timeMin) + ":" + str(timeSec)
    pg.draw.rect(screen, white, pg.Rect(SCREEN_WIDTH - 60, SCREEN_HEIGHT - 40, 60, 40))
    TextDisplays.textDisp2(screen, timeText, black, SCREEN_WIDTH, SCREEN_HEIGHT, 30)