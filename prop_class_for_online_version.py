import threading
import time
import tkinter as tk
import pickle
font = ("Courier", 12)

row_coordinates = {}
column_coordinates = {}

my_places = {'go_box': [], 'old kent road': [], 'community1': [], 'Whitechapel Road': [], 'income_tax': [],
             "King's Cross Station": [], 'The Angel Islington': [], 'chance1': [], 'vermount_avenue': []
    , 'connecticut_avenue': [], 'just_visiting': []
    , 'st_charles_place': [], 'electric_company': [], 'states_avenue': [], 'virginia_avenue': [],
             'pennsylvania_railroad': [], 'st_james_place': [], 'community2': [], 'tennessesse_avenue': [],
             'new_york_avenue': []
    , 'free_parking': [], 'kentucky_avenue': [], 'chance2': [], 'india_avenue': [], 'illinois_avenue': [],
             'b_and_o_railroad': [], 'atlantic_avenue': [], 'ventnor_avenue': [],
             'water_works': [], 'marvin_gardens': [], 'go_to_jail': [],
             'pacific_avenue': [], 'north_carolina_avenue': [], 'community3': [], 'pennsylvania_avenue': [],
             'shortline': [], 'chance3': [], 'park_place': [], 'luxury_tax': [], 'board_walk': [], }

# contains information about properties -- imp for save feaure
prop_info = {}
place_num = {}
# properties apart from normal properties - need special attention
special_properties = ["Chance", "community chest", "jail", "just_visting", "go_to_jail", "water works", "electric company",
                      "go box", "Free Parking", "luxury tax", "income tax!", "kings cross station", "fenchurch st station"
                        , "liverpool_st_station", "marlyebone station", "chance"]

prop_id = {}
place_id_place_to_pos = {}

class my_property_class:
    def __init__(self, main_frame_para, property_str, row, column, width, height, color=None, rent=None, price=None,
                 one_house_rent=None, two_house_rent=None,
                 three_house_rent=None, four_house_rent=None, hotel_rent=None, cost_of_house=None,
                 cost_of_hotel=None, mortgage_value=None, color_box_side=None):
        global main_frame
        main_frame = main_frame_para
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
        self.color_box_side = color_box_side
        self.height = height
        self.width = width
        self.row = row
        self.col = column
        row_coordinates.update({property_str: row})
        column_coordinates.update({property_str: column})

        if self.property_str not in special_properties:
            prop_info.update(
                {self.property_str: {"price": self.price, "houses": 0, "owner": None, "current rent": self.rent, "rent":self.rent }})
            self.prop_box = tk.Frame(main_frame, width=width, height=height, bg=self.color, highlightbackground="black",
                                     highlightthickness=1)
            self.current_rent = prop_info[self.property_str]["current rent"]
            self.prop_box.grid(row=row, column=column)

        if self.property_str in special_properties:
            prop_info.update(
                {self.property_str:None})
            self.prop_box = tk.Frame(main_frame, width=width, height=height, highlightbackground="black",
                                     highlightthickness=1)
            self.prop_box.grid(row=row, column=column)

    def update_dicto(self, prop_obj, pos):
        prop_id.update({pos: prop_obj})
        place_num.update({pos: self.property_str})
        place_id_place_to_pos.update({self.property_str: pos})

    def playerOnSite(self, player_name_para, username_para, client_para ,rd_obj_para, data_holder):
        global username, player_name, client, rd_obj
        rd_obj = rd_obj_para
        client = client_para
        player_name = player_name_para
        username = username_para
        self.property_manager(data_holder)

    def property_manager(self, data_holder):
        self.show_details()
        self.buy_btn_shown = False
        if self.property_str not in special_properties:
            if prop_info[self.property_str]["owner"] is None and player_name == username:
                self.price_btn = tk.Label(main_frame, text ="Price: "+str(self.price), font = font, bg = self.color)
                self.price_btn.grid(row=5, column=8)
                self.buy_btn_shown = True
                self.buy_btn = tk.Button(main_frame, text="Buy", bg=self.color,
                                         command=lambda: self.buy_prop(data_holder))
                self.buy_btn.grid(row=6, column=8)

            if prop_info[self.property_str]["owner"] is not None:
                if prop_info[self.property_str]["owner"] != player_name:
                    print("owner not on site")
                    print(prop_info)
                    if player_name == username:
                        # RENT PROPOSAL
                        client.send(pickle.dumps((username, prop_info[self.property_str]["owner"], self.current_rent,"rent")))
                        rd_obj.end_turn_btn.grid_forget()
                        self.rent_btn = tk.Button(main_frame, text="Give Rent",
                                                  command=lambda: self.give_rent(data_holder), bg=self.color, font=font)
                        self.rent_btn.grid(row=6, column=8)
                        self.rent_timer = tk.Label(main_frame, text = "Pay Rent \nin 150 sec", bg="yellow",font = font)
                        self.rent_timer.grid(row=6, column=9)
                        self.rent_label = tk.Label(main_frame,text = "Rent: "+str(self.current_rent), bg =self.color, font = font)
                        self.rent_paid = False
                        timer_thread = threading.Thread(target=self.pay_rent_timer())
                        timer_thread.start()

                if prop_info[self.property_str]["owner"] == player_name:
                    print("owner on site")
                    print(prop_info)
                    # dev here (build house)

        else:
            # means player on special property
            # dev here , take 200 or tell to go somewhere on board
            pass

    def give_rent(self, data_holder):
        self.rent_paid = True
        self.rent_btn.grid_forget()
        self.rent_label.grid_forget()
        client.send(pickle.dumps((username, "paying rent")))
        time.sleep(0.2)
        client.send(pickle.dumps((username, "money", data_holder["game info"][username]["money"]-self.current_rent)))
        time.sleep(0.4)
        client.send(pickle.dumps((prop_info[self.property_str]["owner"], "money", data_holder["game info"][prop_info[self.property_str]["owner"]]["money"]+self.current_rent )))

    def buy_prop(self, data_holder):
        print("buying property!")
        self.price_btn.grid_forget()
        self.buy_btn.grid_forget()
        prop_info[self.property_str]["owner"] = username
        self.owner_label["text"] = "Owner: " + str(prop_info[self.property_str]["owner"])
        # check if player has enough money
        if data_holder["game info"][player_name]["money"] > self.price:
            prop_info[self.property_str]["owner"] = username
            client.send(pickle.dumps((player_name, "properties", "update", self.property_str)))
            time.sleep(0.5)
            client.send(pickle.dumps((player_name,"money", data_holder["game info"][player_name]["money"]-self.price)))

        else:
            client.send(pickle.dumps((player_name , "coudn't buy", self.property_str, "because of lack of money.")))

    def player_left(self, data_holder_p, player):
        # one of the objects/instances will call this method and make the owner of the props of the left platey to none
         for prop in data_holder_p["game info"][player]["properties"].keys():
             prop_info[prop]["owner"] = None
             prop_info[prop]["current"] = self.rent
             prop_info[prop]["houses"] = 0

    def pay_rent_timer(self):
        t = 150
        while True:
            if self.rent_paid == False:
                t-=1
                self.rent_timer["text"] = f"Pay Rent in \n{t} sec"
                if t == 0:
                    self.rent_timer['text'] = f"Now you will be charged \ndouble rent-{2*self.current_rent},(enjoy)!"
                    self.rent_btn.grid_forget()
                    self.rent_label.grid_forget()
                    rd_obj.show_end_turn_btns()
                    time.sleep(3)
                    self.rent_timer.grid_forget()
                    break
                time.sleep(1)

            else:
                self.rent_timer.grid_forget()
                rd_obj.show_end_turn_btns()
                break

    def show_details(self):
        self.info_box1 = tk.Frame(main_frame, relief="raised", highlightbackground="black",highlightthickness=1)

        self.info_box2 = tk.Frame(main_frame, relief="raised", highlightbackground="black",highlightthickness=1)

        if self.property_str not in special_properties:
            self.info_box1.grid(rowspan=6, columnspan=2, row=4, column=1)
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

            self.price_label = tk.Label(self.info_box2, text="Price: " + str(self.price),
                                               font=("Courier", 12), highlightbackground="black",
                                               highlightthickness=1)
            self.price_label.pack(padx=10)

            self.owner_label = tk.Label(self.info_box2, text="Owner: " + str(prop_info[self.property_str]["owner"]),
                                               font=("Courier", 12), highlightbackground="black",
                                               highlightthickness=1)
            self.owner_label.pack(padx=10)

        else:
            self.info_box1.grid(rowspan=6, columnspan=2, row=4, column=1)
            self.label_of_info_box = tk.Label(self.info_box1, text = "You will be thrown \nto a random position or \n given 200 Rupees", font=font)
            self.label_of_info_box.pack(side="top")


# created the objects below for testing, to see the objects - refer to client file after recv_game_info !
"""
width = main_frame.winfo_screenwidth()  # width of screen
height = main_frame.winfo_screenheight()  # height of screen
width -= 325
height -= 345
width = width / 9
height = height / 9

# top lane

free_parking = my_property_class("Free Parking", 0, 0, 160, 140)
free_parking.update_dicto(free_parking, 20)

strand = my_property_class("Strand", 0, 1, width, 140, "firebrick1", 18, 220,
                           90, 250, 700, 875, 1050, 150, 150, 110, "s")
strand.update_dicto(strand, 21)

chance2 = my_property_class("Chance", 0, 2, width, 140)
chance2.update_dicto(chance2, 22)

fleet_street = my_property_class("fleet street", 0, 3, width, 140, "firebrick1", 18, 220,
                                 90, 250, 700, 875, 1050, 150, 150, 110, "s")
fleet_street.update_dicto(fleet_street, 23)

trafalagar_square = my_property_class("trafalagar square", 0, 4, width, 140, "firebrick1", 20, 240,
                                      100, 300, 750, 925, 1100, 150, 150, 120, "s")
trafalagar_square.update_dicto(trafalagar_square, 24)

fenchurch_st_station = my_property_class("fenchurch st station", 0, 5, width, 140)
fenchurch_st_station.update_dicto(fenchurch_st_station, 25)

licester_square = my_property_class("licester square", 0, 6, width, 140, "yellow", 22, 290,
                                    110, 330, 800, 975, 1150, 150, 150, 130, "s")
licester_square.update_dicto(licester_square, 26)

coventry_street = my_property_class("coventry street", 0, 7, width, 140, "yellow", 22, 290,
                                    110, 330, 800, 975, 1150, 150, 150, 130, "s")
coventry_street.update_dicto(coventry_street, 27)

water_works = my_property_class("water works", 0, 8, width, 140)
water_works.update_dicto(water_works, 28)

piccadilly = my_property_class("piccadilly", 0, 9, width, 140, "yellow", 24, 280,
                               120, 360, 850, 1025, 1200, 150, 150, 140, "s")
piccadilly.update_dicto(piccadilly, 29)

go_to_jail = my_property_class("go_to_jail", 0, 10, 160, 140)
go_to_jail.update_dicto(go_to_jail, 30)

# right lane
regent_street = my_property_class("regent street", 1, 10, 160, height, "green", 26, 300,
                                  130, 390, 900, 1100, 1275, 200, 200, 150, "w")
regent_street.update_dicto(regent_street, 31)

oxford_street = my_property_class("oxford street", 2,10 , 160, height, "green", 26, 300,
                                  130, 390, 900, 1100, 1275, 200, 200, 150, "w")
oxford_street.update_dicto(free_parking, 32)

community_chest = my_property_class("community_chest", 3,10, 160, height)
community_chest.update_dicto(community_chest, 33)

bond_street = my_property_class("bond street", 4, 10, 160, height, "green", 28, 320,
                                150, 450, 1000, 1200, 1400, 200, 200, 160, "w")
bond_street.update_dicto(bond_street, 34)

liverpool_st_station = my_property_class("liverpool_st_station", 5, 10, 160, height)
liverpool_st_station.update_dicto(liverpool_st_station, 35)

chance3 = my_property_class("chance3", 6, 10, 160, height)
chance3.update_dicto(chance3, 36)

park_lane = my_property_class("park_lane", 7, 10, 160, height, "dark blue", 35, 350,
                              175, 500, 1100, 1300, 1500, 200, 200, 175, "w")
park_lane.update_dicto(park_lane, 37)

super_tax = my_property_class("super_tax", 8, 10, 160, height)
super_tax.update_dicto(super_tax, 38)

mayfair = my_property_class("mayfair", 9, 10, 160, height, "dark blue", 50, 400,
                            200, 600, 1400, 1700, 2000, 200, 200, 200, "w")
mayfair.update_dicto(mayfair, 39)

# lower lane\

just_visiting = my_property_class("just_visting", 10, 0, 160, 140)
just_visiting.update_dicto(just_visiting, 10)

pentoville_road = my_property_class("pentoville road", 10, 1, width, 140, "light blue", 8, 120,
                                    40, 100, 300, 450, 600, 50, 50, 60, "n")
pentoville_road.update_dicto(pentoville_road, 9)

euston_road = my_property_class("euston road", 10, 2, width, 140, "light blue", 6, 100,
                                30, 90, 270, 400, 550, 50, 50, 50, "n")
euston_road.update_dicto(euston_road, 8)

chance1 = my_property_class("chance", 10, 3, width, 140)
chance1.update_dicto(chance1, 7)

the_angel_islington = my_property_class("the angel islington", 10, 4, width, 140, "light blue", 6, 100,
                                        30, 90, 270, 400, 550, 50, 50, 50, "n")
the_angel_islington.update_dicto(the_angel_islington, 6)

kings_cross_station = my_property_class("kings cross station", 10, 5, width, 140)
kings_cross_station.update_dicto(kings_cross_station, 5)

income_tax = my_property_class("income tax!", 10, 6, width, 140)
income_tax.update_dicto(income_tax, 4)

white_chapal_road = my_property_class("white chapal road", 10, 7, width, 140, "brown", 4, 60,
                                      20, 60, 180, 320, 450, 50, 50, 30, "n")
white_chapal_road.update_dicto(white_chapal_road, 3)

community_chest1 = my_property_class("community chest", 10, 8, width, 140)
community_chest1.update_dicto(community_chest1, 2)

old_kent_road = my_property_class("old kent road", 10, 9, width, 140, "brown", 2, 60,
                                  10, 30, 90, 160, 250, 50, 50, 30, "n")
old_kent_road.update_dicto(old_kent_road, 1)

go_box = my_property_class("go box", 10, 10, 160, 140)
go_box.update_dicto(go_box, 0)

# left lane

pall_mall = my_property_class("pall mall", 9, 0, 160, height, "pink", 10, 140,
                              50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
pall_mall.update_dicto(pall_mall, 11)

electric_company = my_property_class("electric company", 8, 0, 160, height)
electric_company.update_dicto(electric_company, 12)

white_hall = my_property_class("white hall", 7, 0, 160, height, "pink", 10, 140,
                               50, 150, 450, 625, 750, 100, 50 * 2, 70, "e")
white_hall.update_dicto(white_hall, 13)

northumber_ld_avenue = my_property_class("northumberl'd avenue", 6, 0, 160, height, "pink", 12, 160, 60,
                                         180, 500, 700, 900, 100, 100, 80, "e")
northumber_ld_avenue.update_dicto(northumber_ld_avenue, 14)

marylebone_station = my_property_class("marltbone station",5 , 0, 160, height)
marylebone_station.update_dicto(marylebone_station, 15)

bow_street = my_property_class("bow street", 4, 0, 160, height, "orange", 14, 180,
                               70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
bow_street.update_dicto(bow_street, 16)

community_chest2 = my_property_class("community chest", 3, 0, 160, height)
community_chest2.update_dicto(community_chest2, 17)

marlborough_street = my_property_class("marlborough street",2,0, 160, height, "orange", 14, 180,
                                       70, 200, 550, 750, 950, 100, 50 * 2, 90, "e")
marlborough_street.update_dicto(marlborough_street, 18)

vine_street = my_property_class("vine street", 1, 0, 160, height, "orange", 16, 200,
                                80, 220, 600, 800, 1000, 100, 50 * 2, 100, "e")
vine_street.update_dicto(vine_street, 19)

monopoly_dis = tk.Label(main_frame, text="Monopoly", bg="tomato1", fg="white")
monopoly_dis.grid(row=5, column=5)

sf_width = 8 * width + 2
sf_height = 3 * height
status_frame = tk.LabelFrame(main_frame, text="Status Box", bg="light green", fg="black",
                             highlightbackground="black", highlightthickness=1, width=sf_width,
                             height=sf_height)
status_frame.grid(rowspan=4, columnspan=9, row=1, column=1)

main_frame.mainloop()"""

