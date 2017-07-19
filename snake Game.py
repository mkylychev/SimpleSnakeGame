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
time.sleep(5)
