import pygame
import keyboard,os,random

os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

information = pygame.display.information() # You have to call this before pygame.display.set_mode()
screen_width,screen_height = information.current_w,information.current_h

grey = (211,211,211)
brown = (139,69,19)
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)

gameDisplay = pygame.display.set_mode((screen_width,screen_height))
gameDisplay.fill(grey)

run = True


board_image = pygame.image.load('monopoly board.jpg')
board_image = pygame.transform.scale(board_image, (screen_width,screen_height-20))
gameDisplay.blit(board_image,(0,0))

my_places ={'go_box':" ",'mediteranean_avenue':" ",'community1' :" ",'baltic_avenue':" ",'income_tax':" ",
            'reading_railroad' :" ",'oriental_avenue':" ",'chance1':" ",'vermount_avenue':" "
            ,'connecticut_avenue':" ",'just_visiting':" "
    ,'st_charles_place':" ",'electric_company':" ",'states_avenue':" ",'virginia_avenue':" ",
            'pennsylvania_railroad':" ",'st_james_place':" ",'community2':" ",'tennessesse_avenue':" ",'new_york_avenue':" "
        ,'free_parking':" ",'kentucky_avenue':" ",'chance2':" ",'india_avenue':" ",'illinois_avenue':" ",'b_and_o_railroad':" ",'atlantic_avenue':" ",'ventnor_avenue':" ",
            'water_works':" ",'marvin_gardens':" ",'go_to_jail':" ",
        'pacific_avenue':" ",'north_carolina_avenue':" ",'community3':" ",'pennsylvania_avenue':" ",
            'shortline':" ",'chance3':" ",'park_place':" ",'luxury_tax':" ",'board_walk':" "}

row_coordinates= {}
column_coordinates = {}
myplace_num ={}
myplaces=[]

for place in my_places.keys():
    myplaces.append(str(place))

def leave():
    global run
    pygame.quit()
    run = False

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
#position = (1307,721)
token1 = things(1307,700,30,40,white)

#def show_a_button()
position = 0
def roll_dice():
    global position
    dice_roll = random.randint(0,6)
    position += dice_roll
    if position>=41:
        position -= 41

while run:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            run = False


        mouse = pygame.mouse.get_pos()

        print(mouse)


    pygame.display.update()
    keyboard.add_hotkey('shift+q',leave)
