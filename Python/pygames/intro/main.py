import py
import pygame
from sys import exit
pygame.init()

screen=pygame.display.set_mode((800,400))
pygame.display.set_caption('my first(last) game')
clock=pygame.time.Clock()

test_surface=pygame.image.load('graphics/Sky.png')
# test_surface.fill('Red')

while True:#event loop!
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    screen.blit(test_surface,(0,0))
    clock.tick(60)