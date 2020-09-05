from Display_our_board import *
import pygame


#token1 = rectangles(1250,700,100,50,blue)

def buttons(btn_x,btn_y,btn_w,btn_h,clr,light_clr,text):

    mouse = pygame.mouse.get_pos()

    if btn_x + btn_w >= mouse[0] >= btn_x and btn_y + btn_h >= mouse[1] >= btn_y:
        pygame.draw.rect(gameDisplay,light_clr,[btn_x, btn_y,btn_w,btn_h])

    else:
        pygame.draw.rect(gameDisplay,clr,[btn_x, btn_y,btn_w,btn_h])

