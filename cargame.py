from turtle import width
import pygame
from pygame.locals import *
import random

# intialise pygame
pygame.init

# Game settings 
running = True
size = width, height = (800,800)
road_w = int(width/1.6)
roadmark_w = int(width/80)
right_lane = width/2 + road_w/4
left_lane = width/2 - road_w/4
# animation parameters
speed = 1

# player car
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = right_lane, height*0.8


# other car
car2 = pygame.image.load("otherCar.png")
car2_loc = car2.get_rect()
car2_loc.center = left_lane, height*0.2


#  Set window size
screen =pygame.display.set_mode((800,800))
# Set title
pygame.display.set_caption("Kool car game")
# Set background
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()


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



counter = 0
# Main game loop
while running:
    
    counter += 1
    # increase game difficulty overtime
    if counter == 5000:
        speed += 0.15
        counter = 0
        print("level up", speed)

    # animate other car
    car2_loc[1] += speed
    if car2_loc[1] > height:
        if random.randint(0,1) == 0:
            car2_loc.center = right_lane, -200
        else:
            car2_loc.center = left_lane, -200
    
    # end game logic
    if car_loc[0] == car2_loc[0] and car2_loc[1] > car_loc[1] - 250:
        print("GAME OVER! YOU LOST!")
        break

    # Event Listerner to quit game
    for event in pygame.event.get():
        # quit application
        if event.type == QUIT:
            running = False

        # add keyboard events
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w/2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w/2), 0])

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
    # add car to screen
    screen.blit(car, car_loc)
    screen.blit(car2, car2_loc)
    # apply changes
    pygame.display.update()



# Exit Pygame
pygame.quit