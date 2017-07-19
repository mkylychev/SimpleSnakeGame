import pygame
import sys
import random
import time

# check for init
check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors".format(check_errors[1]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized")

# Play surface
play_surface = pygame.display.set_mode((720, 460))
pygame.display.set_caption('Snake game')
time.sleep(2)

# Colors

red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
brown = pygame.Color(165, 25, 25)

# FPS controller

fpsConroller = pygame.time.Clock()

snakePos = [100, 50]
snakeBody = [[100, 50], [90, 50], [80, 50]]

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
foodSpawn = True

diraction = 'RIGHT'
changeto = diraction


# Game over function

def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    play_surface.blit(GOsurf, GOrect)
    pygame.display.flip()

gameOver()
time.sleep(10)
