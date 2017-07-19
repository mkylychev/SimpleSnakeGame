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
score = 0


# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)
    GOsurf = myFont.render('Game over!', True, red)
    GOrect = GOsurf.get_rect()
    GOrect.midtop = (360, 15)
    play_surface.blit(GOsurf, GOrect)
    showScore(0)
    pygame.display.flip()
    time.sleep(4)
    pygame.quit()
    sys.exit()


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score: ' + str(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    play_surface.blit(Ssurf, Srect)



# gameOver()
# time.sleep(10)
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
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    if changeto == 'RIGHT' and not diraction == 'LEFT':
        diraction = 'RIGHT'
    if changeto == 'LEFT' and not diraction == 'RIGHT':
        diraction = 'LEFT'
    if changeto == 'UP' and not diraction == 'DOWN':
        diraction = 'UP'
    if changeto == 'DOWN' and not diraction == 'UP':
        diraction = 'DOWN'

    if diraction == 'RIGHT':
        snakePos[0] += 10
    if diraction == 'LEFT':
        snakePos[0] -= 10
    if diraction == 'UP':
        snakePos[1] -= 10
    if diraction == 'DOWN':
        snakePos[1] += 10

    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score +=1
        foodSpawn = False
    else:
        snakeBody.pop()
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

    play_surface.fill(white)
    for pos in snakeBody:
        pygame.draw.rect(play_surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(play_surface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[0] == block[1]:
            gameOver()

    showScore()
    pygame.display.flip()

    fpsConroller.tick(10)
