

#h_or_v = {}

# for the grid positions of all places on the board!

row_coordinates = {}
column_coordinates = {}
myplace_num = {}
place_num = {}
myplaces = []
"""
for place in my_places.keys():
    myplaces.append(str(place))

for horizontal_lane in myplaces[0:11]:
    h_or_v.update({horizontal_lane:"H"})

for vertical_lane in myplaces[11:20]:
    h_or_v.update({vertical_lane: "V"})

for horizontal_lane in myplaces[20:31]:
    h_or_v.update({horizontal_lane:"H"})

for vertical_lane in myplaces[31:40]:
    h_or_v.update({vertical_lane:"V"})

# working properly-
# print(h_or_v)
"""

i = 0
for p in myplaces:
    myplace_num.update({p: i})
    i += 1

for k,v in myplace_num.items():
    place_num.update({v:k})
print(place_num)
# go till jail
c1 = 10
for pl in myplaces[0:11]:  # changed 12 to 11
    column_coordinates.update({pl: c1})
    row_coordinates.update({pl: 10})
    c1 -= 1

# st_charles till new york avenue
r1 = 10
for pl in myplaces[11:20]:
    column_coordinates.update({pl: 0})
    row_coordinates.update({pl: r1})
    r1 -= 1

# free parking till go to jail
c2 = 0
for pl in myplaces[20:31]:  # changed 32 to 31
    column_coordinates.update({pl: c2})
    row_coordinates.update({pl: 0})
    c2 += 1

# pacific till board walk
r2 = 2
for pl in myplaces[31:40]:
    column_coordinates.update({pl: 10})
    row_coordinates.update({pl: r2})
    r2 += 1











"""
print(row_coordinates)
print(column_coordinates)

inverted_row_dict = {}
inverted_column_dict = {}

for place,r in row_coordinates.items():
    inverted_row_dict.update({r:place})

for place,c in column_coordinates.items():
    inverted_column_dict.update({c:place})

print(inverted_row_dict)
print(inverted_column_dict)"""



# for place functionaity
"""
place_x = {}
place_y = {}

for place in myplaces[0:11]:
    place_y.update({place:285})

place_x.update({"go_box":590})
place_x.update({'mediteranean_avenue':450})

x = 450-120
for place in myplaces[2:9]:
    place_x.update({place:x})
    x-=120

place_x.update({'connecticut_avenue': -500})
place_x.update({'just_visiting': -640})

for place in myplaces[11:20]:
    place_x.update({place:-640})

place_y.update({"st_charles_place":180})

y = 140
for place in myplaces[12:20]:
    place_y.update({place:y})
    y-=50

for place in myplaces[20:31]:
    place_y.update({place:-300})

place_x.update({"free_parking":-640})
place_x.update({"kentucky_avenue":-500})

x = -500 + 120
for place in myplaces[22:30]:
    place_x.update({place:x})
    x += 120

place_x.update({"go_to_jail":580})

for place in myplaces[31:40]:
    place_x.update({place:580})

place_y.update({"go_to_jail":-300})
place_y.update({"pacific_avenue":-205})

y = -205 + 50
for place in myplaces[32:38]:
    place_y.update({place:y})
    y+=50

place_y.update({"luxury_tax":135})
place_y.update({"board_walk":185})




# working properly -
print(place_x)
print(place_y)

import TOKEN
screen_width = TOKEN.root.winfo_screenwidth() #width of screen
screen_height = TOKEN.root.winfo_screenheight() # height of screen

# for setting width and height of property boxes

width = {}
height = {}

w = screen_width - 320
w = int(w / 9)
h = screen_height-340
h = int(h/9)

width.update({"go_box":160})
for place in myplaces[1:10]:
    width.update({place:w})
width.update({"just_visiting":160})

for place in myplaces[0:11]:
    height.update({place:140})

for place in myplaces[11:20]:
    width.update({place:160})

for place in myplaces[12:19]:
    height.update({place:h})

width.update({"free_parkling":160})
for place in myplaces[21:30]:
    width.update({place:w})
width.update({"go_to_jail":160})

for place in myplaces[20:31]:
    height.update({place:140})

for place in myplaces[32:41]:
    width.update({place:160})

for place in myplaces[31:41]:
    height.update({place:h})

# for place function[place()]
place_x = {}
place_y = {}
print(width)
print(height)
go_box = screen_width - width["go_box"]
print(go_box)

"""



























