import tkinter as tk

def step_2(main_frame,font1, player_chances, player_names, chance,colors, n_players):

    # contains information about properties -- imp for save feaure
    prop_info = {}
    # properties apart from normal properties - need special attention
    special_properties = ["chance", "community chest", "jail", "go_to_jail", "water works", "electric company", "go box", "free parking", "luxury tax", "income tax"]
    class my_property_class:
        def __init__(self,property_str, row, column, width, height, color, rent, price, one_house_rent, two_house_rent,
                     three_house_rent,four_house_rent,hotel_rent,cost_of_house,cost_of_hotel, mortgage_value, color_box_side=None):
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
    # (self, my_property_class_id, my_property_class_str, row, column, buying_price, rent, house_price, one_house_rent, color_group)

    free_parking = tk.Frame(main_frame, width=160, height=140, bg="orange", highlightbackground="black",
                            highlightthickness=1)
    free_parking.grid(row=0, column=0)

    kentucky_avenue = my_property_class("kentucky_avenue", 0, 1, width, 140, "light blue", 100, 200,
                                                       50, 60, 70, 80, 100, 100, 50, 40, "bottom")

    # chance2 = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1", highlightbackground="black",
    #                   highlightthickness=1)
    # chance2_obj = my_property_class(chance2, "chance2", 0, 2)
    # chance2.grid(row=0, column=2)

    chance2 = my_property_class("Chance", 0, 2, width, 140, "orange", 0, 0, 100, 200, 50, 60, 70, 80,
                                               100, 70)

    indiana_avenue = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                              highlightbackground="black",
                              highlightthickness=1)
    # indiana_avenue_obj = my_property_class(indiana_avenue, "indiana_avenue", 0, 3)
    indiana_avenue.grid(row=0, column=3)
    illinois_avenue = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                               highlightbackground="black",
                               highlightthickness=1)
    # illinois_avenue_obj = my_property_class(illinois_avenue, "illinois_avenue", 0, 4)
    illinois_avenue.grid(row=0, column=4)
    b_and_o_railroad = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                                highlightbackground="black",
                                highlightthickness=1)
    b_and_o_railroad.grid(row=0, column=5)
    # b_and_o_railroad_obj = my_property_class(b_and_o_railroad, "b_and_o_railroad", 0, 5)

    atlantic_avenue = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                               highlightbackground="black",
                               highlightthickness=1)
    # atlantic_avenue_obj = my_property_class(atlantic_avenue, "atlantic_avenue", 0, 6)
    atlantic_avenue.grid(row=0, column=6)
    ventnor_avenue = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                              highlightbackground="black",
                              highlightthickness=1)
    # ventnor_avenue_obj = my_property_class(ventnor_avenue, "ventnor_avenue", 0, 7)
    ventnor_avenue.grid(row=0, column=7)

    water_works = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                           highlightbackground="black",
                           highlightthickness=1)
    # water_works_obj = my_property_class(water_works, "water_works", 0, 8)
    water_works.grid(row=0, column=8)

    marvin_garden = tk.Frame(main_frame, width=width, height=140, bg="LightSteelBlue1",
                             highlightbackground="black",
                             highlightthickness=1)
    # marvin_garden_obj = my_property_class(marvin_garden, "marvin_garden", 0, 9)
    marvin_garden.grid(row=0, column=9)

    go_to_jail = tk.Frame(main_frame, width=160, height=140, bg="yellow", highlightbackground="black",
                          highlightthickness=1)
    # go_to_jail_obj = my_property_class(go_to_jail, "go_to_jail", 0, 10)
    go_to_jail.grid(row=0, column=10)

    # left lane
    new_york_avenue = tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue",
                               highlightbackground="black", highlightthickness=1)
    # global new_york_avenue_obj
    # new_york_avenue_obj = my_property_class(new_york_avenue, "pacific_avenue", 1, 0)
    new_york_avenue.grid(row=1, column=0)

    tennessee_avenue = tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue",
                                highlightbackground="black",
                                highlightthickness=1)
    # tennessee_avenue_obj = my_property_class(tennessee_avenue, "tennessee_avenue", 2, 0)
    tennessee_avenue.grid(row=2, column=0)

    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=3, column=0)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=4, column=0)
    tk.Frame(main_frame, width=160, height=height, bg='green', highlightbackground="black",
             highlightthickness=1).grid(row=5, column=0)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=6, column=0)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=7, column=0)
    tk.Frame(main_frame, width=160, height=height, bg="lightsteelblue", highlightbackground="black",
             highlightthickness=1).grid(row=8, column=0)
    tk.Frame(main_frame, width=160, height=height, bg="yellow", highlightbackground="black",
             highlightthickness=1).grid(row=9, column=0)

    # lower lane
    just = tk.Frame(main_frame, width=160, height=140, bg="pink", highlightbackground="black",
                    highlightthickness=1).grid(row=10, column=0)
    place3 = tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
                      highlightthickness=1)
    place3.grid(row=10, column=1)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=2)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=3)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=4)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=5)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=6)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=7)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=8)
    tk.Frame(main_frame, width=width, height=140, bg="pink", highlightbackground="black",
             highlightthickness=1).grid(row=10, column=9)
    go_box = tk.Frame(main_frame, width=160, height=140, bg="brown", highlightbackground="black",
                      highlightthickness=1)
    go_box.grid(row=10, column=10)

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
                                 highlightbackground="black", highlightthickness=1, width=sf_width,
                                 height=sf_height)
    status_frame.grid(rowspan=4, columnspan=9, row=1, column=1)

    global properties_dicto
    properties_dicto = {21: kentucky_avenue, 22: chance2}

    import class_token, initialising_everything
    class_token.step_3(main_frame,status_frame,properties_dicto, n_players, initialising_everything.playing_tokens,colors,sf_width,sf_height)

    import roll_dice
    roll_dice.step_5(main_frame, font1, n_players, properties_dicto)

