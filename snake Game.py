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
    time.sleep(4)
    pygame.quit()
    sys.exit()


gameOver()
time.sleep(10)
# Main logic
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))

    if changeto == 'RIGHT' and not diraction == 'LEFT':
        diraction = 'RIGHT'
    if changeto == 'LEFT' and not diraction == 'RIGHT':
        diraction = 'RIGHT'
    if changeto == 'UP' and not diraction == 'DOWN':
        diraction = 'UP'
    if changeto == 'DOWN' and not diraction == 'UP':
        diraction = 'DOWN'

    if diraction == 'RIGHT':
        snakePos[0] += 10
    if diraction == 'LEFTT':
        snakePos[0] -= 10
    if diraction == 'UP':
        snakePos[1] -= 10
    if diraction == 'DOWN':
        snakePos[1] += 10


