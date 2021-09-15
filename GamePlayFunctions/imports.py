from BoardFunctions.BoardCheckContinue import BoardCheckContinue
from BoardFunctions.BoardGenerateFull import BoardGenerateFull
from BoardFunctions.BoardGenerateRandom import BoardGenerateRandom
from BoardFunctions.BoardSolver import BoardSolver
from GUIFunctions.InputBoxes import InputBox as GUIInputBox
from GUIFunctions.BoardDisplay import boardDisplay as GUIBoardDisplay
from GUIFunctions.DrawGrid import drawGrid as GUIDrawGrid
from GUIFunctions.Quitbutton import quitButton as GUIQuitButton
from GUIFunctions.SolveButton import solveButton as GUISolveButton
from GUIFunctions.ReturnButton import returnButton as GUIReturnButton
from GUIFunctions.TimeDisplay import timeDisplay as GUITimeDisplay
from GUIFunctions.TextDisplays import textDisp as GUITextDisplayOne
from GUIFunctions.TextDisplays import textDisp2 as GUITextDisplayTwo
from GUIFunctions.TextDisplays import failDisp as GUIFailDisplay
import copy
from GlobalImports import *



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

