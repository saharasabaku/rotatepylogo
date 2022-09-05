""" draw_rect1.py """
import sys
import pygame
from math import sin, cos, radians
from pygame.locals import QUIT, Rect

pygame.init()
SURFACE = pygame.display.set_mode((300, 300))
FPSCLOCK = pygame.time.Clock()

def main():
    """ main routine """
    logo = pygame.image.load("pythonlogo.jpg")
    theta = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        
        SURFACE.fill((255, 255, 255))
        #ここから

        theta -= 1

        new_logo = pygame.transform.rotate(logo, theta)
        rect = new_logo.get_rect()
        rect.center = (150, 150)
        SURFACE.blit(new_logo, rect)


        #ここまで
        pygame.display.update()
        FPSCLOCK.tick(280)

if __name__ == '__main__':
    main()
