import tkinter as tk


def step_2(main_frame, font1, player_chances, player_names, chance, colors, n_players):
    # contains information about properties -- imp for save feaure
    prop_info = {}
    # properties apart from normal properties - need special attention
    special_properties = ["chance", "community chest", "jail", "go_to_jail", "water works", "electric company",
                          "go box", "free parking", "luxury tax", "income tax"]

    class my_property_class:
        def __init__(self, property_str, row, column, width, height, color=None, rent=None, price=None, one_house_rent=None, two_house_rent=None,
                     three_house_rent=None, four_house_rent=None, hotel_rent=None, cost_of_house=None, cost_of_hotel=None, mortgage_value=None,
                     color_box_side=None):
            self.property_str = property_str
            self.width = width
            self.height = height
            self.one_house_rent = one_house_rent
            self.two_house_rent = two_house_rent
            self.three_house_rent = three_house_rent
            self.four_house_rent = four_house_rent
            self.hotel_rent = hotel_rent
            self.cost_of_hotel = cost_of_hotel
            self.mortgage_value = mortgage_value
            self.price = price
            self.color = color
            self.rent = rent
            self.cost_of_house = cost_of_house

            prop_info.update(
                {self.property_str: {"price": self.price, "houses": 0, "owner": None, "players on site": []}})

            if self.property_str not in special_properties:
                self.prop_box = tk.Frame(main_frame, width=width, height=height, highlightbackground="black",
                                         highlightthickness=1)
                self.prop_box.grid(row=row, column=column)
                self.color_box = tk.Frame(main_frame, bg=self.color, highlightbackground="black", highlightthickness=1,
                                          width=self.width, height=self.height / 4)
                self.color_box.grid(row=row, column=column, sticky="s")
                self.buy_button = tk.Button(main_frame, text="Buy", bg=self.color, font=font1,
                                            command=lambda: self.buy_prop())

            if self.property_str in special_properties:
                pass

        def property_manager(self):
            self.show_details()
            prop_info[self.property_str]["players on site"] = player_names[player_chances[chance]]

            if prop_info[self.property_str]["owner"] == None:
                self.buy_button.grid(row=6, column=8)

            if prop_info[self.property_str]["owner"] != None:
                if prop_info[self.property_str]["owner"] == prop_info[self.property_str]["players on site"][-1]:
                    print("non owner on site")
                    print(prop_info)
                    # dev here (TRADE option or build house)
                if prop_info[self.property_str]["owner"] == prop_info[self.property_str]["players on site"][-1]:
                    print("owner on site")
                    print(prop_info)
                    # dev here (take rent)

        def buy_prop(self):
            print("buying property!")
            self.buy_button.grid_forget()
            prop_info[self.property_str]["owner"] = player_chances[chance]
            tk.Label(main_frame, text=player_chances[chance] + " successfully bought-" + self.property_str,
                     bg=self.color).grid(columnspan=3, row=6, column=6)
            print(prop_info)

        def show_details(self):

            self.info_box1 = tk.Frame(main_frame, relief="raised", highlightbackground="black", width=width * 4,
                                      height=height * 4,
                                      highlightthickness=1)
            self.info_box1.grid(rowspan=6, columnspan=2, row=4, column=1)

            self.info_box2 = tk.Frame(main_frame, relief="raised", highlightbackground="black", width=width * 4,
                                      height=height * 4,
                                      highlightthickness=1)
            self.info_box2.grid(rowspan=6, columnspan=2, row=4, column=3)

            self.prop_name_dis = tk.Label(self.info_box1, text=self.property_str, bg=self.color, font=("Courier", 12),
                                          highlightbackground="black",
                                          highlightthickness=1)
            self.prop_name_dis.pack(side="top", fill="x")

            self.rent_dis = tk.Label(self.info_box1, text="RENT- SITE ONLY: " + str(self.rent), font=("Courier", 12),
                                     highlightbackground="black",
                                     highlightthickness=1)
            self.rent_dis.pack(side="top")

            self.house1 = tk.Label(self.info_box1, text="RENT- with 1 house: " + str(self.one_house_rent),
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.house1.pack(side="top")
            self.house2 = tk.Label(self.info_box1, text="RENT-with 2 houses: " + str(self.two_house_rent),
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.house2.pack(side="top")

            self.house3 = tk.Label(self.info_box1, text="RENT-with 3 houses: " + str(self.three_house_rent),
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.house3.pack(side="top")
            self.house4 = tk.Label(self.info_box1, text="RENT-with 4 houses: " + str(self.four_house_rent),
                                   font=("Courier", 12), highlightbackground="black",
                                   highlightthickness=1)
            self.house4.pack(side="top")

            self.hotel = tk.Label(self.info_box2, text="RENT- with HOTEL: " + str(self.hotel_rent),
                                  font=("Courier", 12), highlightbackground="black",
                                  highlightthickness=1)
            self.hotel.pack(side="top")

            self.cost_of_house_dis = tk.Label(self.info_box2, text="cost of one house: " + str(self.cost_of_house),
                                              font=("Courier", 12), highlightbackground="black",
                                              highlightthickness=1)
            self.cost_of_house_dis.pack(side="top")

            self.cost_hotel = tk.Label(self.info_box2,
                                       text="cost of hotel: " + str(self.cost_of_hotel) + "\n+four houses",
                                       font=("Courier", 12), highlightbackground="black",
                                       highlightthickness=1)
            self.cost_hotel.pack(side="top")

            self.mortgage_value_dis = tk.Label(self.info_box2, text="Mortgage value: " + str(self.mortgage_value),
                                               font=("Courier", 12), highlightbackground="black",
                                               highlightthickness=1)
            self.mortgage_value_dis.pack(side="top")

    width = main_frame.winfo_screenwidth()  # width of screen
    height = main_frame.winfo_screenheight()  # height of screen
    width -= 325
    height -= 345
    width = width / 9
    height = height / 9
    free_parking = my_property_class("Free Parking", 0, 0, 160, 140)

    strand = my_property_class("Strand", 1, 0, width, 140, "firebrick1", 18, 220,
                               90, 250, 700, 875, 1050, 150, 150, 110, "bottom")

    chance2 = my_property_class("Chance", 2, 0, width, 140)

    fleet_street = my_property_class("fleet street", 3, 0, width, 140, "firebrick1", 18, 220,
                                     90, 250, 700, 875, 1050, 150, 150, 110, "bottom")

    trafalagar_square = my_property_class("trafalagar square", 4, 0, width, 140, "firebrick1", 20, 240,
                                          100, 300, 750, 925, 1100, 150, 150, 120, "bottom")

    fenchurch_st_station = my_property_class("fenchurch st station", 5, 0, width, 140)

    licester_square = my_property_class("licester square", 6, 0, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "bottom")

    coventry_street = my_property_class("coventry street", 7, 0, width, 140, "yellow", 22, 290,
                                        110, 330, 800, 975, 1150, 150, 150, 130, "bottom")

    water_works = my_property_class("water works", 8, 0, width, 140)

    piccadilly = my_property_class("piccadilly", 9, 0, width, 140, "yellow", 24, 280,
                                   120, 360, 850, 1025, 1200, 150, 150, 140, "bottom")

    go_to_jail = my_property_class("go_to_jail", 10, 0, width, 140)

    # left lane
    regent_street = my_property_class("regent street", 10, 1, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "left")

    oxford_street = my_property_class("oxford street", 10, 2, 160, height, "green", 26, 300,
                                      130, 390, 900, 1100, 1275, 200, 200, 150, "left")

    community_chest = my_property_class("community_chest", 10, 3, 160, height)

    bond_street = my_property_class("bond street", 10, 4, 160, height, "green", 28, 320,
                                    150, 450, 1000, 1200, 1400, 200, 200, 160, "left")

    liverpool_st_station = my_property_class("liverpool_st_station", 10, 5, 160, height)

    chance3 = my_property_class("chance3", 10, 6, 160, height)

    park_lane = my_property_class("park_lane", 10, 7, 160, height, "dark blue", 35, 350,
                                  175, 500, 1100, 1300, 1500, 200, 200, 175, "bottom")

    super_tax = my_property_class("super_tax", 10, 8, 160, height)

    mayfair = my_property_class("mayfair", 10, 9, 160, height, "dark blue", 50, 400,
                                200, 600, 1400, 1700, 2000, 200, 200, 200, "bottom")

    # lower lane
    just_visiting = my_property_class("just_visting", 10, 0, 160, 140)

    pentoville_road = my_property_class("pentoville road", 10, 1, width, 140, "light blue", 8, 120,
                                        40,100, 300, 450, 600, 50, 50, 60, "bottom")

    euston_road = my_property_class("euston road", 10, 2, width, 140, "light blue", 6, 100,
                                    30, 90, 270, 400, 550, 50, 50, 50, "bottom")
    
    chance1 = ("chance", 10, 3, width, 140)
    the_angel_islington = my_property_class("the angel islington", 10, 4, width, 140, "light blue", 6, 100,
                                    30, 90, 270, 400, 550, 50, 50, 50, "bottom")

    kings_cross_station = my_property_class("kings cross station", 10, 5, width, 140)

    income_tax = my_property_class("income tax!", 10, 6, width, 140)

    white_chapal_road = my_property_class("white chapal road", 10, 7, width, 140, "brown", 4, 60,
                                          20, 60, 180, 320, 450, 50, 50, 30, "bottom")

    community_chest1 = my_property_class("community chest", 10, 8, width, 140)

    old_kent_road = my_property_class("old kent road", 10, 9, width, 140, "brown", 2, 60,
                                      10, 30, 90, 160, 250, 50, 50, 30, "bottom")

    go_box = my_property_class("go box", 10, 10, 160, 140)

    # right lane
    pall_mall = my_property_class("pall mall", 0, 9, 160, height, "pink", 10, 140,
                                  50, 150, 450, 625, 750, 100, 50*2, 70, "bottom")
    electric_company = my_property_class("electric company", 0, 8, 160, height)

    white_hall = my_property_class("white hall", 0, 7, 160, height, "pink", 10, 140,
                                  50, 150, 450, 625, 750, 100, 50*2, 70, "bottom")

    northumber_ld_avenue = my_property_class("northumberl'd avenue", 0, 6, 160, height, "pink", 12,160, 60,
                                             180, 500, 700, 900, 100, 100, 80,  "bottom")

    marylebone_station = my_property_class("marltbone station", 0, 5, 160, height)

    bow_street = my_property_class("bow street", 0, 4, 160, height, "orange", 14, 180,
                                   70, 200, 550, 750, 950, 100, 50*2,90, "bottom")

    community_chest2 = my_property_class("community chest", 0, 3, 160, height)
    marlborough_street = my_property_class("marlborough street", 0, 2, 160, height, "orange", 14, 180,
                                   70, 200, 550, 750, 950, 100, 50*2,90, "bottom")
    vine_street = my_property_class("vine street", 0, 1, 160, height, "orange", 16, 200,
                                    80, 220, 600, 800, 1000, 100, 50*2, 100, "bottom")


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
    class_token.step_3(main_frame, status_frame, properties_dicto, n_players, initialising_everything.playing_tokens,
                       colors, sf_width, sf_height)

    import roll_dice
    roll_dice.step_5(main_frame, font1, n_players, properties_dicto)

