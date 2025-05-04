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

coin = pygame.image.load("C:/Pygame2/images/coin.png")
coin = pygame.transform.scale(coin,(35,35))
coinx = 335
coiny = -45
coin_rect = pygame.Rect(coinx,coiny,35,35) 

rock = pygame.image.load("C:/Pygame2/images/rock.png")
rock = pygame.transform.scale(rock,(35,35))
rockx = 135
rocky = -45
rock_rect = pygame.Rect(rockx,rocky,35,35)

clock = pygame.time.Clock()

run = True

velocity = 1.5

font = pygame.font.SysFont("comicsans",45)

score = 0

while run == True:

    Score = font.render("Score: "+str(score),1,"white")
    coin_rect = pygame.Rect(coinx,coiny,35,35)
    car_rect = pygame.Rect(carx,cary,45,75)  
    rock_rect = pygame.Rect(rockx,rocky,35,35)
    clock.tick(100)
    screen.blit(road,(roadx,roady))
    screen.blit(sidebars,(sidebarx,sidebary))
    screen.blit(sidebars2,(siderbar2x,sidebar2y))
    screen.blit(car,(carx,cary))
    screen.blit(rock,(rockx,rocky))
    screen.blit(coin,(coinx,coiny))
    screen.blit(Score,(90,45))
    sidebary = sidebary + velocity
    sidebar2y = sidebar2y + velocity
    roady = roady + velocity
    coiny = coiny + velocity
    rocky = rocky + velocity

    if sidebary > 0 or sidebar2y > 0 or roady > 0:
        sidebary = -190
        sidebar2y = -190
        roady = -150
    if coin_rect.colliderect(car_rect):
        coiny = -35
        score = score + 1
        j = random.randint(1,2)
        if j == 1:
            coinx = 135
        if j == 2:
            coinx = 335
    if coiny > 500:
        coiny = -35
        j = random.randint(1,2)
        if j == 1:
            coinx = 135
        if j == 2:
            coinx = 335

    if rock_rect.colliderect(car_rect):
        rocky = -35
        score = score - 1
        r = random.randint(1,2)
        if r == 1:
            rockx = 135
        if r == 2:
            rockx = 335
    if rocky > 500:
        rocky = -35
        r = random.randint(1,2)
        if r == 1:
            rockx = 135
        if r == 2:
            rockx = 335
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                carx = 335
            if event.key == K_LEFT:
                carx = 135


    pygame.display.flip()
    


