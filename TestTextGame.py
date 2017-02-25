import TextGame
import pygame
import sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((1150,725))
FPSCLOCK = pygame.time.Clock()

def main(type):
    if type == 'box':
        box = TextGame.TextBox('Hello Text World!')
        box.update(DISPLAYSURF)
        x = 0
        while True:
            box.change_text('Hello Text World * ' + str(x))
            x += 1
            box.update(DISPLAYSURF)
            FPSCLOCK.tick(2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event == QUIT:
                    exit()
                    pygame.quit()
                    sys.exit()
    elif type == 'choice':
        box = TextGame.ChoiceTextBox(2,['1','2'],'Hello Choices World!')
        box.update(DISPLAYSURF)
        answer = None
        while answer != '1':
            box.update(DISPLAYSURF)
            for event in pygame.event.get():
                if event == MOUSEBUTTONUP:
                    mousePos = event.pos
            answer,number = box.get_button_pressed(mousePos)
            FPSCLOCK.tick(30)
            pygame.display.flip()
    elif type == 'nameBox':
        box = TextGame.NameTextBox('Hello name text boxes world!!!','CC')
        box.update(DISPLAYSURF)
        x = 0
        while True:
            box.change_name(str(x))
            x += 1
            box.update(DISPLAYSURF)
            FPSCLOCK.tick(2)
            pygame.display.flip()
            for event in pygame.event.get():
                if event == QUIT:
                    pygame.quit()
                    sys.exit()

main('choice')