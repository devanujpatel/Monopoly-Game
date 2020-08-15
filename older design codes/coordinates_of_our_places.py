my_places = {'go_box': [],'mediteranean_avenue': [],'community1': [],'baltic_avenue': [],'income_tax': [],
             'reading_railroad': [],'oriental_avenue': [],'chance1': [],'vermount_avenue': []
    , 'connecticut_avenue': [],'just_visiting': []
    , 'st_charles_place': [],'electric_company': [],'states_avenue': [],'virginia_avenue': [],
             'pennsylvania_railroad': [],'st_james_place': [],'community2': [],'tennessesse_avenue':  [],
             'new_york_avenue':  []
    , 'free_parking': [],'kentucky_avenue': [],'chance2': [],'india_avenue': [],'illinois_avenue': [],
             'b_and_o_railroad': [],'atlantic_avenue': [],'ventnor_avenue': [],
             'water_works': [],'marvin_gardens': [],'go_to_jail':  [],
             'pacific_avenue': [],'north_carolina_avenue': [],'community3': [],'pennsylvania_avenue':  [],
             'shortline': [],'chance3': [],'park_place': [],'luxury_tax': [],'board_walk':  []}

row_coordinates = {}
column_coordinates = {}
myplace_num = {}
myplaces = []

for place in my_places.keys():
    myplaces.append(str(place))

# go till jail
c1 = 10
for pl in myplaces[0:11]:  # changed 12 to 11
    column_coordinates.update({pl: c1})
    row_coordinates.update({pl: 11})
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
    row_coordinates.update({pl: 1})
    c2 += 1

# pacific till board walk
r2 = 2
for pl in myplaces[31:40]:
    column_coordinates.update({pl: 10})
    row_coordinates.update({pl: r2})
    r2 += 1

i = 0
for p in myplaces:
    myplace_num.update({p: i})
    i += 1