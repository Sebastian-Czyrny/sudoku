from .imports import *


def importPlay():
    board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    emptyBoard = copy.deepcopy(board)

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
            if board[i][j] == 0:
                inputBoxes[i].append(GUIInputBox(GRID_BOX * j, GRID_BOX * i, GRID_BOX, GRID_BOX))

    returnPress = GUIReturnButton(3*SCREEN_WIDTH/4 - 75, SCREEN_HEIGHT - 90, 150, 50)
    solvePress = GUISolveButton(SCREEN_WIDTH/4 - 75, SCREEN_HEIGHT - 90, 150, 50)

    screen.fill(white)
    GUIDrawGrid(screen)
    pg.display.update()

    while returnPress.keepGoing:
        mouse = pg.mouse.get_pos()

        for event in pg.event.get():
            if event.type == pg.QUIT: exit()

            if not solvePress.boardSolvedCheck():
                for list in inputBoxes[:]:
                    for box in list:
                        box.handle_event_import(event, board)
            if not solvePress.boardSolvedCheck():
                for list in inputBoxes[:]:
                    for box in list:
                        box.draw_import(screen)

            returnPress.handle_event(event, mouse)
            solvePress.handle_event_import(event, mouse, screen, board)

        GUIDrawGrid(screen)

        returnPress.draw(mouse, screen)
        solvePress.draw(mouse, screen)

        pg.display.flip()