from turtle import width
import pygame
from pygame.locals import *

# intialise pygame
pygame.init

# Game settings 
running = True
size = width, height = (800,800)
road_w = int(width/1.6)
roadmark_w = int(width/80)

# player car
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/2 + road_w/4, height*0.8


# other car
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = width/2 - road_w/4, height*0.8


#  Set window size
screen =pygame.display.set_mode((800,800))
# Set title
pygame.display.set_caption("Kool car game")
# Set background
screen.fill((60, 220, 0))


# draw graphics
pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2, 0, road_w, height))

# draw centre line
pygame.draw.rect(
    screen,
    (255, 240, 60),
    (width/2 - roadmark_w/2, 0, roadmark_w, height))
# draw left road marking
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 - road_w/2 + roadmark_w*2, 0, roadmark_w, height))
# draw right road marking
pygame.draw.rect(
    screen,
    (255, 255, 255),
    (width/2 + road_w/2 - roadmark_w*3, 0, roadmark_w, height))



# apply changes
pygame.display.update()



while running:
    for event in pygame.event.get():
        # quit application
        if event.type == QUIT:
            running = False

    # add car to screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()



# Exit Pygame
pygame.quit