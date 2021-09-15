
from .imports import *
import copy


def playerPlay():
    # initialze the boards
    completeBoard = BoardGenerateFull()
    playerBoard = BoardGenerateRandom(copy.deepcopy(completeBoard))

    inputBoxes = [[],
                [],
                [],
                [],
                [],
                [],
                [],
                [],
                []
    ]
    for i in range(9):
        for j in range(9):
            if playerBoard[i][j] == 0:
                inputBoxes[i].append(GUIInputBox(GRID_BOX * j, GRID_BOX * i, GRID_BOX, GRID_BOX))


    # initialize the clock
    playerTime = pg.time.Clock()
    timeElapsed = 0

    returnPress = GUIReturnButton(3*SCREEN_WIDTH/4 - 75, SCREEN_HEIGHT - 90, 150, 50)
    solvePress = GUISolveButton(SCREEN_WIDTH/4 - 75, SCREEN_HEIGHT - 90, 150, 50)

    screen.fill(white)

    GUIBoardDisplay(screen, playerBoard, grey)
    GUIDrawGrid(screen)
    pg.display.update()

    boardChecked = False

    while returnPress.keepGoing:
        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT: exit()

            returnPress.handle_event(event, mouse)
            solvePress.handle_event(event, mouse, screen, playerBoard, completeBoard)
            if not boardChecked:
                if solvePress.boardSolvedCheck():
                    playerBoard = completeBoard
                    boardChecked = True

            # input buttons
            if not solvePress.boardSolvedCheck(): # if board has been completed or not
                for list in inputBoxes[:]:
                    for box in list:
                        box.handle_event(event, playerBoard, completeBoard)

        if not solvePress.boardSolvedCheck():
            for list in inputBoxes[:]:
                for box in list:
                    box.draw(screen, solvePress.boardSolvedCheck())

        GUIFailDisplay(screen, inputBoxes)

        GUIDrawGrid(screen)

        returnPress.draw(mouse, screen)
        solvePress.draw(mouse, screen)
        if not solvePress.boardSolvedCheck():
            timeElapsed += playerTime.tick()
        GUITimeDisplay(timeElapsed, screen)

        pg.display.flip()