import pygame
import sys
import random
import time

check_errors = pygame.init()

if check_errors[1] > 0:
    print("(!) Had {0} initializing errors".format(check_errors[1]))
    sys.exit(-1)
else:
    print("PyGame successfully initialized")

