from BoardFunctions.BoardCheckContinue import BoardCheckContinue
from BoardFunctions.BoardGenerateFull import BoardGenerateFull
from BoardFunctions.BoardGenerateRandom import BoardGenerateRandom
from GUIFunctions.BoardDisplay import boardDisplay as GUIBoardDisplay
from GUIFunctions.DrawGrid import drawGrid as GUIDrawGrid
from GUIFunctions.Quitbutton import quitButton as GUIQuitButton
from GUIFunctions.TextDisplays import textDisp as GUITextDisplayOne
from GamePlayFunctions.PlayerPlay import playerPlay
from GamePlayFunctions.ImportPlay import importPlay
from GlobalImports import *



def main():

    boardMain = BoardGenerateFull()
    boardMain = BoardGenerateRandom(boardMain)

    screen.fill(white)

    GUIBoardDisplay(screen, boardMain, grey)
    GUIDrawGrid(screen)
    pg.display.update()

    quitPress = GUIQuitButton(SCREEN_WIDTH/2 - 50, SCREEN_HEIGHT- 60, 100, 50)

    while True:
        screen.fill(white)
        GUIBoardDisplay(screen, boardMain, grey)
        GUIDrawGrid(screen)

        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT: exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                # PLAY BUTTON
                if (SCREEN_WIDTH/4 -50) <= mouse[0] <= (SCREEN_WIDTH/4 + 50) and (SCREEN_HEIGHT - 125) <= mouse[1] <= (SCREEN_HEIGHT - 75):
                    playerPlay()
                # IMPORT BUTTON
                elif (3*SCREEN_WIDTH/4 - 60) <= mouse[0] <= (3*SCREEN_WIDTH/4 + 60) and (SCREEN_HEIGHT - 125) <= mouse[1] <= (SCREEN_HEIGHT - 75):
                    importPlay()

            quitPress.handle_event(event,mouse
            )
        # PLAY BUTTON RECT
        if (SCREEN_WIDTH/4 -50) <= mouse[0] <= (SCREEN_WIDTH/4 + 50) and (SCREEN_HEIGHT - 125) <= mouse[1] <= (SCREEN_HEIGHT - 75):
            pg.draw.rect(screen, lightGrey, pg.Rect(SCREEN_WIDTH/4 -50, SCREEN_HEIGHT - 125, 100, 50))
        else:
            pg.draw.rect(screen, grey, pg.Rect(SCREEN_WIDTH/4 -50, SCREEN_HEIGHT - 125, 100, 50))

        # IMPORT BUTTON RECT
        if (3*SCREEN_WIDTH/4 - 60) <= mouse[0] <= (3*SCREEN_WIDTH/4 + 60) and (SCREEN_HEIGHT - 125) <= mouse[1] <= (SCREEN_HEIGHT - 75):
            pg.draw.rect(screen, lightGrey, pg.Rect(3*SCREEN_WIDTH/4 - 60, SCREEN_HEIGHT - 125, 120, 50))
        else:
            pg.draw.rect(screen, grey, pg.Rect(3*SCREEN_WIDTH/4 - 60, SCREEN_HEIGHT - 125, 120, 50))

        # QUIT BUTTON RECT
        quitPress.draw(mouse, screen)



        GUITextDisplayOne(screen, "PLAY", black, SCREEN_WIDTH/4, SCREEN_HEIGHT-100, 30)
        GUITextDisplayOne(screen, "IMPORT", black, 3*SCREEN_WIDTH/4, SCREEN_HEIGHT-100, 30 )

        pg.display.flip()





if __name__ == '__main__':
    main()
    pg.quit()