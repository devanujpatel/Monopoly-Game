my_places = {'go_box': [],'mediteranean_avenue': [],'community1': [],'baltic_avenue': [],'income_tax': [],
             'reading_railroad': [],'oriental_avenue': [],'chance1': [],'vermount_avenue': []
    , 'connecticut_avenue': [],'just_visiting': []
    , 'st_charles_place': [],'electric_company': [],'states_avenue': [],'virginia_avenue': [],
             'pennsylvania_railroad': [],'st_james_place': [],'community2': [],'oxford_street':  [],
             'regent_street':  []
    , 'free_parking': [],'strand': [],'chance2': [],'trafalagar_square': [],'illinois_avenue': [],
             'b_and_o_railroad': [],'licester_square': [],'coventry_street': [],
             'water_works': [],'piccadilly': [],'go_to_jail':  [],
             'pacific_avenue': [],'north_carolina_avenue': [],'community3': [],'pennsylvania_avenue':  [],
             'shortline': [],'chance3': [],'park_place': [],'luxury_tax': [],'board_walk':  [], }

import tkinter as tk

def step_2(main_frame,font1, player_chances, player_names, chance,colors, n_players):

    # contains information about properties -- imp for save feaure
    prop_info = {}
    # properties apart from normal properties - need special attention
    special_properties = ["chance", "community chest", "jail", "go_to_jail", "water works", "electric company", "go box", "free parking", "luxury tax", "income tax"]
    class my_property_class:
        #def __init__(self,property_str, row, column, width, height, color=None, rent=None, price=None, one_house_rent=None, two_house_rent=None,
        #             three_house_rent=None,four_house_rent=None,hotel_rent=None,cost_of_house=None,cost_of_hotel=None, mortgage_value=None, color_box_side=None):

        def __init__(self,property_str="", row=None, column=None, width=None, height=None, color="", rent=None, price=None, one_house_rent=None, two_house_rent=None,
                     three_house_rent=None,four_house_rent=None,hotel_rent=None,cost_of_house=None,cost_of_hotel=None, mortgage_value=None, color_box_side=""):
            self.property_str = property_str
            self.width = width
            self.height = height
            self.one_house_rent = one_house_rent
            self.two_house_rent  = two_house_rent
            self.three_house_rent = three_house_rent
            self.four_house_rent = four_house_rent
            self.hotel_rent = hotel_rent
            self.cost_of_hotel = cost_of_hotel
            self.mortgage_value = mortgage_value
            self.price = price
            self.color= color
            self.rent = rent
            self.cost_of_house = cost_of_house
            prop_info.update({self.property_str:{"price":self.price, "houses":0, "owner":None, "players on site":[]}})
            print("prop info",prop_info)
    
            if self.property_str not in special_properties:
                self.prop_box = tk.Frame(main_frame, width=width, height=height,highlightbackground="black" ,highlightthickness=1)
                self.prop_box.grid(row=row, column=column)
                self.color_box = tk.Frame(main_frame, bg=self.color,highlightbackground="black" ,highlightthickness=1 , width=self.width, height=self.height/4)
                self.color_box.grid(row=row, column=column, sticky = "s")
                self.buy_button = tk.Button(main_frame, text="Buy", bg=self.color,font=font1 , command=lambda :self.buy_prop())

            if self.property_str in special_properties:
                pass



        def property_manager(self):
            self.show_details()
            prop_info[self.property_str]["players on site"] = player_names[player_chances[chance]]

            if prop_info[self.property_str]["owner"] == None:
                self.buy_button.grid(row=6, column=8)

            if prop_info[self.property_str]["owner"] != None:
                if prop_info[self.property_str]["owner"] ==  prop_info[self.property_str]["players on site"][-1]:
                    print("non owner on site")
                    print(prop_info)
                    # dev here (TRADE option or build house)
                if prop_info[self.property_str]["owner"] ==  prop_info[self.property_str]["players on site"][-1]:
                    print("owner on site")
                    print(prop_info)
                    # dev here (take rent)

        def buy_prop(self):
            print("buying property!")
            self.buy_button.grid_forget()
            prop_info[self.property_str]["owner"] = player_chances[chance]
            tk.Label(main_frame, text=player_chances[chance]+" successfully bought-"+self.property_str,bg=self.color).grid(columnspan=3,row=6,column=6)
            print(prop_info)

        def show_details(self):

            self.info_box1 = tk.Frame(main_frame, relief="raised", highlightbackground="black",width = width*4, height=height*4,
                              highlightthickness=1)
            self.info_box1.grid(rowspan = 6,columnspan=2,  row = 4, column = 1)

            self.info_box2 = tk.Frame(main_frame, relief="raised", highlightbackground="black",width = width*4, height=height*4,
                              highlightthickness=1)
            self.info_box2.grid(rowspan = 6,columnspan=2,  row = 4, column = 3)


            self.prop_name_dis = tk.Label(self.info_box1, text=self.property_str, bg=self.color ,font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.prop_name_dis.pack(side="top" , fill="x")

            self.rent_dis = tk.Label(self.info_box1, text="RENT- SITE ONLY: "+str(self.rent), font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.rent_dis.pack(side="top" )

            self.house1 = tk.Label(self.info_box1, text="RENT- with 1 house: "+str(self.one_house_rent), font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.house1.pack(side="top" )
            self.house2 = tk.Label(self.info_box1, text="RENT-with 2 houses: "+str(self.two_house_rent), font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.house2.pack(side="top" )

            self.house3 = tk.Label(self.info_box1, text="RENT-with 3 houses: "+str(self.three_house_rent), font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.house3.pack(side="top" )
            self.house4 = tk.Label(self.info_box1, text="RENT-with 4 houses: "+str(self.four_house_rent), font=("Courier", 12), highlightbackground="black",
                              highlightthickness=1)
            self.house4.pack(side="top" )

            self.hotel = tk.Label(self.info_box2, text="RENT- with HOTEL: " + str(self.hotel_rent) ,
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.hotel.pack(side="top" )

            self.cost_of_house_dis = tk.Label(self.info_box2, text="cost of one house: " + str(self.cost_of_house) ,
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.cost_of_house_dis.pack(side="top" )


            self.cost_hotel = tk.Label(self.info_box2, text="cost of hotel: " + str(self.cost_of_hotel)+"\n+four houses",
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.cost_hotel.pack(side="top" )


            self.mortgage_value_dis = tk.Label(self.info_box2, text="Mortgage value: " + str(self.mortgage_value) ,
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.mortgage_value_dis.pack(side="top" )

    width = main_frame.winfo_screenwidth()  # width of screen
    height = main_frame.winfo_screenheight()  # height of screen
    width -= 325
    height -= 345
    width = width / 9
    height = height / 9

    free_parking = my_property_class("Free Parking", 0, 0, 160)

    strand = my_property_class("Strand", 0, 1, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    chance2 = my_property_class("Chance", 0, 2, width, 140)

    fleet_street = my_property_class("fleet street", 0, 3, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    trafalagar_square = my_property_class("trafalagar square", 0, 4, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    fenchurch_st_station = my_property_class("fenchurch st station", 0, 5, width, 140)

    licester_square = my_property_class("licester square", 0, 6, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    
    coventry_street = my_property_class("coventry street", 0, 7, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    water_works = my_property_class("water works", 0, 8, width, 140)

    piccadilly = my_property_class("piccadilly", 0, 9, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    go_to_jail = my_property_class("go_to_jail", 0, 10, width, 140)
 
    # left lane
    regent_street = my_property_class("regent street", 10,1, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")
   
    oxford_street = my_property_class("oxford street", 10, 2, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    community_chest = my_property_class("community_chest", 10, 3, width, 140)

    bond_street = my_property_class("bond street", 10, 4, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    liverpool_st_station = my_property_class("liverpool_st_station", 10, 5, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    chance3 = my_property_class("chance3", 10, 6, width, 140)

    park_lane = my_property_class("park_lane", 10, 7, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    super_tax = my_property_class("super_tax", 10, 8, width, 140)

    mayfair = my_property_class("mayfair", 10, 9, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    # lower lane
    just_visiting = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    pentoville_road = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                                                     50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    euston_road=my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    chance1 = ("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    the_angel_islington = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    kings_cross_station = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    income_tax = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    white_chapal_road = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    community_chest1 = my_property_class("just_visting", 10, 9, width, 140)
    old_kent_road = my_property_class("just_visting", 10, 9, width, 140, "light blue", 100, 200,
                      50, 60, 70, 80, 100, 100, 50, 40, "bottom")
    go_box = my_property_class("just_visting", 10, 9)
    # right lane
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=1, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=2, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=3, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=4, column=10)
    tk.Frame(main_frame, width=160, height=height, bg='green', highlightbackground="black",
             highlightthickness=1).grid(row=5, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=6, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=7, column=10)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=8, column=10)
    place = tk.Frame(main_frame, width=160, height=height, bg="yellow", highlightbackground="black",
                     highlightthickness=1)
    place.grid(row=9, column=10)




    monopoly_dis = tk.Label(main_frame, text="Monopoly", bg="tomato1", fg="white", font=font1)
    monopoly_dis.grid(row=5, column=5)

    sf_width = 8 * width + 2
    sf_height = 3 * height
    status_frame = tk.LabelFrame(main_frame, text="Status Box", bg="light green", fg="black",
                                 highlightbackground="black", highlightthickness=1, width=sf_width,height=sf_height)
    status_frame.grid(rowspan=4, columnspan=9, row=1, column=1)

    global properties_dicto
    properties_dicto = {21: strand, 22: chance2}

    import class_token, initialising_everything
    class_token.step_3(main_frame,status_frame,properties_dicto, n_players, initialising_everything.playing_tokens,colors,sf_width,sf_height)



