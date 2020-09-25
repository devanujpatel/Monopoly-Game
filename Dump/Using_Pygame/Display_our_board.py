# This code will be imported in Mono_Board_pygame

import pygame,os

# to set the width and height to fit our screen
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

# Assign variables to store our width and height
info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h

gameDisplay = pygame.display.set_mode((screen_width,screen_height))

# Show our Board!!
board_image = pygame.image.load('monopoly board.jpg')
board_image = pygame.transform.scale(board_image, (screen_width,screen_height-20))
gameDisplay.blit(board_image,(0,0))