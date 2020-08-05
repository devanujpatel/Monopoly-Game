import pygame, keyboard,os,random
from information import *

# to set the width and height to fit our screen
os.environ['SDL_VIDEO_CENTERED'] = '1' # You have to call this before pygame.init()

pygame.init()

info = pygame.display.Info()
screen_width,screen_height = info.current_w,info.current_h

gameDisplay = pygame.display.set_mode((screen_width,screen_height))

# will run the main loop
run = True

board_image = pygame.image.load('monopoly board.jpg')
board_image = pygame.transform.scale(board_image, (screen_width,screen_height-20))
gameDisplay.blit(board_image,(0,0))

# a dictioanry including all the places on the board!!!
my_places ={'go_box':" ",'mediteranean_avenue':" ",'community1' :" ",'baltic_avenue':" ",'income_tax':" ",
            'reading_railroad' :" ",'oriental_avenue':" ",'chance1':" ",'vermount_avenue':" "
            ,'connecticut_avenue':" ",'just_visiting':" "
    ,'st_charles_place':" ",'electric_company':" ",'states_avenue':" ",'virginia_avenue':" ",
            'pennsylvania_railroad':" ",'st_james_place':" ",'community2':" ",'tennessesse_avenue':" ",'new_york_avenue':" "
        ,'free_parking':" ",'kentucky_avenue':" ",'chance2':" ",'india_avenue':" ",'illinois_avenue':" ",'b_and_o_railroad':" ",'atlantic_avenue':" ",'ventnor_avenue':" ",
            'water_works':" ",'marvin_gardens':" ",'go_to_jail':" ",
        'pacific_avenue':" ",'north_carolina_avenue':" ",'community3':" ",'pennsylvania_avenue':" ",
            'shortline':" ",'chance3':" ",'park_place':" ",'luxury_tax':" ",'board_walk':" "}

#in this dictionary we will add pixel coordinates of eachplace on the board!
pixels_cords= {}

#this dictionary will contain a unique identity no. for each place on the board
# which is the no. of the places from go box with go box being 0
myplace_id ={}

# to
id = 0
for place in my_places.keys():
    myplace_id.update({place:id})
    id += 1
# every token starts form the go box thus initial positon = 0
position = 0

# for the purpose of storing our places in a list (might be of some help in future)
myplaces=[]
for place in my_places.keys():
    myplaces.append(str(place))

#to quit the game and make run = False so we stop our main loop of game
def leave():
    global run
    pygame.quit()
    run = False

# to make a function which we will use to make rectangles for our tokens easily.
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

# we call the above defined function to make a rectangle
token1 = things(1307,700,30,40,blue)

#to show_a_button()

def roll_dice():
    global position
    # we random a no. to simulate dice roll
    dice_roll = random.randint(0,6)
    # adding the the dice roll to position
    position += dice_roll
    # if postion exceeds 40 (which is the last position onn our board) then we
    if position >= 41:
        position -= 41

while run:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            run = False


        mouse = pygame.mouse.get_pos()

        print(mouse)


    pygame.display.update()
    keyboard.add_hotkey('shift+q',leave)
