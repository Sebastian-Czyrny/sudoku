from .imports import *
from . import TextDisplays
from . import BoardDisplay
from . import DrawGrid
import copy


class solveButton:

    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y , w, h)
        self.boardSolved = False


    def handle_event(self, event, mouse, screen, playerBoard, completeBoard):
        if event.type == pg.MOUSEBUTTONDOWN and not self.boardSolved:
            if self.rect.collidepoint(event.pos):
                BoardFunctions.BoardSolver.BoardSolver(completeBoard)
                
                DrawGrid.drawGrid(screen)
                BoardDisplay.boardDisplay(screen, playerBoard, white, completeBoard=completeBoard, solving=True)
                playerBoard = completeBoard

                self.boardSolved = True


    def handle_event_import(self, event, mouse, screen, importBoard):
        if event.type == pg.MOUSEBUTTONDOWN and not self.boardSolved:
            if self.rect.collidepoint(event.pos):
                if BoardFunctions.BoardIsValid.ImportIsValid(importBoard):
                    boardBeforeSolve = copy.deepcopy(importBoard)

                    #start the solving timer
                    solveTime = pg.time.Clock()
                    timeElapsed = 0
                    solveTime.tick()


                    BoardFunctions.BoardSolver.BoardSolver(importBoard)

                    timeElapsed += solveTime.tick()
                    timeText = "Solved in: " + str(timeElapsed) + "ms"
                    pg.draw.rect(screen, white, pg.Rect(SCREEN_WIDTH - 100, SCREEN_HEIGHT - 40, 100, 40))
                    TextDisplays.textDisp2(screen, timeText, black, SCREEN_WIDTH, SCREEN_HEIGHT, 30)

                    BoardDisplay.boardDisplay(screen, boardBeforeSolve, white, completeBoard=importBoard, solving=True)
                    self.boardSolved = True
                else:
                    print("Error")


    def draw(self, mouse, screen):
        if self.boardSolved or (self.rect.x <= mouse[0] <= self.rect.x + self.rect.w and self.rect.y <= mouse[1] <= self.rect.y + self.rect.h):
            pg.draw.rect(screen, lightGrey, self.rect)

        else:
            pg.draw.rect(screen, grey, self.rect)

        if self.boardSolved:
            TextDisplays.textDisp(screen, 'SOLVED', black, self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, 30)
        else:
            TextDisplays.textDisp(screen, 'SOLVE', black, self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, 30)

    def boardSolvedCheck(self):
        if self.boardSolved:
            return True
        else:
            return False