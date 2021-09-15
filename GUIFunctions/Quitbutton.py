from .imports import *
from . import TextDisplays

class quitButton:

    def __init__(self, x, y, w, h):
        self.rect = pg.Rect(x, y , w, h)


    def handle_event(self, event, mouse):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                pg.quit()

    def draw(self, mouse, screen):
        if (self.rect.x <= mouse[0] <= self.rect.x + self.rect.w and self.rect.y <= mouse[1] <= self.rect.y + self.rect.h):
            pg.draw.rect(screen, lightGrey, self.rect)

        else:
            pg.draw.rect(screen, grey, self.rect)

        TextDisplays.textDisp(screen, 'QUIT', black, self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, 30)