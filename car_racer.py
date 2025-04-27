import pygame
from pygame.locals import*
import time
import random
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((500,500))

sidebars = pygame.image.load("C:/Pygame2/images/sidebars.png")
sidebars = pygame.transform.scale(sidebars,(75,700))
sidebarx = 0
sidebary = -190

sidebars2 = pygame.image.load("C:/Pygame2/images/sidebars.png")
sidebars2 = pygame.transform.scale(sidebars2,(76,700))
siderbar2x = 425
sidebar2y = -190

road = pygame.image.load("C:/Pygame2/images/road.png")
road = pygame.transform.scale(road,(510,700))
roadx = -5
roady = 0

car = pygame.image.load("C:/Pygame2/images/car.png")
car = pygame.transform.scale(car,(45,75))
carx = 135
cary = 400
car_rect = pygame.Rect(carx,cary,45,75) 

clock = pygame.time.Clock()

run = True

while run == True:
    clock.tick(375)
    screen.blit(road,(roadx,roady))
    screen.blit(sidebars,(sidebarx,sidebary))
    screen.blit(sidebars2,(siderbar2x,sidebar2y))
    screen.blit(car,(carx,cary))
    sidebary = sidebary + 1.5
    sidebar2y = sidebar2y + 1.5
    roady = roady + 1.5


    if sidebary > 0 or sidebar2y > 0 or roady > 0:
        sidebary = -190
        sidebar2y = -190
        roady = -150
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                carx = 335
            if event.key == K_LEFT:
                carx = 135


    pygame.display.flip()
    


