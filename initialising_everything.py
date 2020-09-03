master_dictionary = {}
colors = {"token1":"firebrick1", "token2":"RoyalBlue2","token3":"orange red" ,"token4":"green2", "token5":"gold","token6":"deep pink","token7":"purple1","token8":"midnight blue"}
playing_tokens = []
all_colors = ['AntiqueWhite1','green' ,"brown", "orange",'AntiqueWhite2', 'AntiqueWhite3', 'AntiqueWhite4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3', 'CadetBlue4', 'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4', 'DarkOliveGreen1', 'DarkOliveGreen2', 'DarkOliveGreen3', 'DarkOliveGreen4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3', 'DarkSeaGreen4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4', 'DeepPink2', 'DeepPink3', 'DeepPink4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4', 'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'IndianRed1', 'IndianRed2', 'IndianRed3', 'IndianRed4', 'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4', 'LightCyan2', 'LightCyan3', 'LightCyan4', 'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4', 'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'LightSkyBlue1', 'LightSkyBlue2', 'LightSkyBlue3', 'LightSkyBlue4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3', 'LightSteelBlue4', 'LightYellow2', 'LightYellow3', 'LightYellow4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3', 'MediumOrchid4', 'MediumPurple1', 'MediumPurple2', 'MediumPurple3', 'MediumPurple4', 'MistyRose2', 'MistyRose3', 'MistyRose4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4', 'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'OrangeRed2', 'OrangeRed3', 'OrangeRed4', 'PaleGreen1', 'PaleGreen2', 'PaleGreen3', 'PaleGreen4', 'PaleTurquoise1', 'PaleTurquoise2', 'PaleTurquoise3', 'PaleTurquoise4', 'PaleVioletRed1', 'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'PeachPuff2', 'PeachPuff3', 'PeachPuff4', 'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3', 'SlateBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3', 'SlateGray4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4', 'SteelBlue1', 'SteelBlue2', 'SteelBlue3', 'SteelBlue4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4', 'alice blue', 'antique white', 'aquamarine', 'aquamarine2', 'aquamarine4', 'azure', 'azure2', 'azure3', 'azure4', 'bisque', 'bisque2', 'bisque3', 'bisque4', 'blanched almond', 'blue', 'blue violet', 'blue2', 'blue4', 'brown1', 'brown2', 'brown3', 'brown4', 'burlywood1', 'burlywood2', 'burlywood3', 'burlywood4', 'cadet blue', 'chartreuse2', 'chartreuse3', 'chartreuse4', 'chocolate1', 'chocolate2', 'chocolate3', 'coral', 'coral1', 'coral2', 'coral3', 'coral4', 'cornflower blue', 'cornsilk2', 'cornsilk3', 'cornsilk4', 'cyan', 'cyan2', 'cyan3', 'cyan4', 'dark goldenrod', 'dark green', 'dark khaki', 'dark olive green', 'dark orange', 'dark orchid', 'dark salmon', 'dark sea green', 'dark slate blue', 'dark slate gray', 'dark turquoise', 'dark violet', 'deep pink', 'deep sky blue', 'dim gray', 'dodger blue', 'firebrick1', 'firebrick2', 'firebrick3', 'firebrick4', 'floral white', 'forest green', 'gainsboro', 'ghost white', 'gold', 'gold2', 'gold3', 'gold4', 'goldenrod', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4', 'gray', 'gray1', 'gray10', 'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19', 'gray2', 'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28', 'gray29', 'gray3', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37', 'gray38', 'gray39', 'gray4', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47', 'gray48', 'gray49', 'gray5', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56', 'gray57', 'gray58', 'gray59', 'gray6', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65', 'gray66', 'gray67', 'gray68', 'gray69', 'gray7', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74', 'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray8', 'gray80', 'gray81', 'gray82', 'gray83', 'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray9', 'gray90', 'gray91', 'gray92', 'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99', 'green yellow', 'green2', 'green3', 'green4', 'honeydew2', 'honeydew3', 'honeydew4', 'hot pink', 'indian red', 'ivory2', 'ivory3', 'ivory4', 'khaki', 'khaki1', 'khaki2', 'khaki3', 'khaki4', 'lavender', 'lavender blush', 'lawn green', 'lemon chiffon', 'light blue', 'light coral', 'light cyan', 'light goldenrod', 'light goldenrod yellow', 'light grey', 'light pink', 'light salmon', 'light sea green', 'light sky blue', 'light slate blue', 'light slate gray', 'light steel blue', 'light yellow', 'lime green', 'linen', 'magenta2', 'magenta3', 'magenta4', 'maroon', 'maroon1', 'maroon2', 'maroon3', 'maroon4', 'medium aquamarine', 'medium blue', 'medium orchid', 'medium purple', 'medium sea green', 'medium slate blue', 'medium spring green', 'medium turquoise', 'medium violet red', 'midnight blue', 'mint cream', 'misty rose', 'navajo white', 'navy', 'old lace', 'olive drab', 'orange', 'orange red', 'orange2', 'orange3', 'orange4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'pale goldenrod', 'pale green', 'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff', 'pink', 'pink1', 'pink2', 'pink3', 'pink4', 'plum1', 'plum2', 'plum3', 'plum4', 'powder blue', 'purple', 'purple1', 'purple2', 'purple3', 'purple4', 'red', 'red2', 'red3', 'red4', 'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1', 'salmon2', 'salmon3', 'salmon4', 'sandy brown', 'sea green', 'seashell2', 'seashell3', 'seashell4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'sky blue', 'slate blue', 'slate gray', 'snow', 'snow2', 'snow3', 'snow4', 'spring green', 'steel blue', 'tan1', 'tan2', 'tan4', 'thistle', 'thistle1', 'thistle2', 'thistle3', 'thistle4', 'tomato', 'tomato2', 'tomato3', 'tomato4', 'turquoise', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'violet red', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'white smoke', 'yellow', 'yellow green', 'yellow2', 'yellow3', 'yellow4']
#player_names = {"player1":"", "player2":"","player3":"","player4":"","player5":"","player6":"","player7":"","player8":""}
player_names = {}
chance = 0
sticky_id = {"token1": "N", "token2": "S", "token3": "w", "token4": "e", "token5": "NE", "token6": "NW", "token7": "SW",
             "token8": "se"}
relx = {}
rely = {}
place_id = []
properties = {}
playing_token_id = []
players=[]

"""
import tkinter
root=tkinter.Tk()# dump everything in master dictionary when going to make save feature
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen
print(width)
print(height)
root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))
frame = tkinter.Frame(root,width=200,height=150,bg='blue')
frame.grid(row=0,column=0)
label = tkinter.Label(root,text="T1!",width=2,height=1)
b = tkinter.Label(root,text="T1!",width=2,height=1)
a = tkinter.Label(root,text="T1!",width=2,height=1)
label.place(in_=frame,relx=0,rely=0,anchor="s")
a.place(in_=frame,relx=0,rely=0,anchor="s")
b.place(in_=frame,relx=0,rely=0,anchor="w")
root.mainloop()
tkinter.Label(root,text="590,285").place(relx=0.5,rely=0.5,x=590,y=285)
tkinter.Label(root,text="450,285").place(relx=0.5,rely=0.5,x=450,y=285)
tkinter.Label(root,text="330,285").place(relx=0.5,rely=0.5,x=330,y=285)
tkinter.Label(root,text="210,285").place(relx=0.5,rely=0.5,x=210,y=285)
tkinter.Label(root,text="90,285").place(relx=0.5,rely=0.5,x=100,y=285)
tkinter.Label(root,text="-500,285").place(relx=0.5,rely=0.5,x=-500,y=285)
tkinter.Label(root,text="-640,285").place(relx=0.5,rely=0.5,x=-640,y=285)

tkinter.Label(root,text="-640,180").place(relx=0.5,rely=0.5,x=-640,y=180)
tkinter.Label(root,text="-640,140").place(relx=0.5,rely=0.5,x=-640,y=140)
tkinter.Label(root,text="-640,90").place(relx=0.5,rely=0.5,x=-640,y=90)
tkinter.Label(root,text="-640,40").place(relx=0.5,rely=0.5,x=-640,y=40)
tkinter.Label(root,text="-10").place(relx=0.5,rely=0.5,x=-640,y=-10)
tkinter.Label(root,text="-640,-220").place(relx=0.5,rely=0.5,x=-640,y=-210)
tkinter.Label(root,text="-640,-300").place(relx=0.5,rely=0.5,x=-640,y=-300)

tkinter.Label(root,text="-500,-300").place(relx=0.5,rely=0.5,x=-500,y=-300)
tkinter.Label(root,text="-380,-300").place(relx=0.5,rely=0.5,x=-380,y=-300)
tkinter.Label(root,text="-260,-300").place(relx=0.5,rely=0.5,x=-260,y=-300)

tkinter.Label(root,text="580,-300").place(relx=0.5,rely=0.5,x=580,y=-300)
tkinter.Label(root,text="580,-205").place(relx=0.5,rely=0.5,x=580,y=-205)
tkinter.Label(root,text="580,-10").place(relx=0.5,rely=0.5,x=580,y=-10)
tkinter.Label(root,text="580,-155").place(relx=0.5,rely=0.5,x=580,y=-155)"""


#     def init_dictos(self,player_str, token_str,token):
#         master_dictionary["tokens"][token_str] = {}
#         master_dictionary["players"][player_str] = {}
# token_str = ('token1','token2','token3','token4','token5','token6','token7','token8')
# master_dictionary["tokens"][token_str[token]] = {"row":row_coordinates[""go_box""], "column": column_coordinates[""go_box""]}
# row = row_coordinates["go_box"_num[position_on_board]]
# column = column_coordinates["go_box"_num[position_on_board]]
#         token_tuple = (token1,token2,token3,token4,token5,token6,token7,token8)
#         token_str = ('token1','token2','token3','token4','token5','token6','token7','token8')
#         player_str = ('player1','player2','player3','player4','player5','player6','player7','player8')
#     """      for token in range(n_players):
#             master_dictionary["tokens"][token_str[token]] = {"position": 0, "row": row_coordinates['"go_box"'],"column": column_coordinates['place'],"token_id":token_tuple[token]}
#             master_dictionary["players"][player_str[token]] = {"token": token_tuple[token], "money": 1500}
#             token_tuple[token].grid(row=10, column=10)"""
# row=master_dictionary["tokens"][token_str]["row"],column=master_dictionary["tokens"][token_str]["column"]










