from .imports import *


# for when the user plays the actual game, this will be the interactive board
class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y , w, h)
        self.color = black
        self.text = text
        self.txt_surface = smallFont.render(text, True, self.color, None)
        self.active = False
        self.value = 0
        self.Locked = False
        self.x = x
        self.y = y
        self.fontType = 'small'
        self.col = int(x/GRID_BOX)
        self.row = int(y/GRID_BOX)
        self.fails = 0

    def handle_event(self, event, playerBoard, completeBoard):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.

        if event.type == pg.KEYDOWN:
            if self.active and not self.Locked:
                if event.key == pg.K_RETURN and len(self.text) == 1:
                    self.txt_surface = bigFont.render(self.text, True, self.color, None)
                    self.fontType = 'big'
                    self.value = int(self.text)
                    self.Locked = True
                    self.boardUpdate(playerBoard, completeBoard)
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                    self.txt_surface = smallFont.render(self.text, True, self.color, None)
                elif event.key in numberKeys:
                    self.text += event.unicode
                    if self.text[len(self.text)-1] in self.text[:len(self.text)-1]:
                        self.text = self.text[:-1]
                # Re-render the text.
                    self.txt_surface = smallFont.render(self.text, True, self.color, None)




    def boardUpdate(self, playerBoard, completeBoard):

        playerBoard[self.row][self.col] = self.value
        if self.value != completeBoard[self.row][self.col]:
            self.Locked = False
            self.text = ''
            self.fontType = 'small'
            self.value = 0
            playerBoard[self.row][self.col] = 0
            self.fails += 1



    def draw(self, screen, boardSolved):
        # Blit the text.
        if not self.active:
            pg.draw.rect(screen, white, self.rect)
        else:
            pg.draw.rect(screen, yellow, self.rect)

        text = self.txt_surface
        textRect = text.get_rect()
        if self.fontType == 'big':
            textRect.center = (self.x + 25, self.y + 25)
            screen.blit(text, textRect)
        else:
            dh = 0
            dx = 0
            for i,num in enumerate(self.text):
                text = smallFont.render(num, True, self.color, None)
                textRect = text.get_rect()
                textRect.left = self.x + 5 + 8 * (i - dx)
                textRect.top = self.y + 2 + dh
                screen.blit(text, textRect)
                if textRect.width * (i + 2 - dx) > 45:
                    dh += textRect.height
                    dx += 5



    # for when the user types down a custom board to be solved by computer
    def handle_event_import(self, event, board):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.


        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE and len(self.text) == 1:
                    self.text = self.text[:-1]
                    board[self.row][self.col] = 0

                elif event.key in numberKeys and len(self.text) == 0:
                    self.text += event.unicode
                    board[self.row][self.col] = int(self.text)
                # Re-render the text.
                self.txt_surface = bigFont.render(self.text, True, self.color, None)

    def draw_import(self, screen):
        if not self.active and not len(self.text) == 1:
            pg.draw.rect(screen, white, self.rect)
        elif not self.active and len(self.text) == 1:
            text = self.txt_surface
            textRect = text.get_rect()
            pg.draw.rect(screen, grey, self.rect)
            textRect.center = (self.x + 25, self.y + 25)
            screen.blit(text, textRect)
        elif self.active and not len(self.text) == 1:
            pg.draw.rect(screen, yellow, self.rect)
        elif self.active and len(self.text) == 1:
            text = self.txt_surface
            textRect = text.get_rect()
            pg.draw.rect(screen, yellow, self.rect)
            textRect.center = (self.x + 25, self.y + 25)
            screen.blit(text, textRect)