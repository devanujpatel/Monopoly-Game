import tkinter as tk

class Player:
    # this class is meant only for display updates
    def __init__(self, main_frame_para,stat_box_para,dicto_para):
        # this is the same main frame from client file code
        global main_frame, stat_box, dicto
        dicto = dicto_para
        stat_box = stat_box_para
        main_frame = main_frame_para

        self.player_name = player_name
        self.client = client_conn
        self.player_chance = player_chance
        self.color = fav_color
        self.dis_token()
        self.sb_width = width * 8
        self.sb_height = height * 3

    def dis_token(self):
        # display our token on the go box
        self.token = tk.Label(main_frame,text ="T"+str(self.player_chance+1),bg = self.color,highlightbackground="black", highlightthickness=1 )
        self.token.grid(row=10, column=10)

    def delete_player(self):
        # will code this a bit later
        pass

    def dis_stat_init(self, n_players):

        # display smaller frame inside our stat box
        self.inferior_status_frame = tk.LabelFrame(stat_box, text=self.player_name, bg=self.color,relief="flat",
                                                   width=self.sb_width / n_players, height=self.sb_height, font=("white", 13),bd=7)

        # fill the small box with information
        self.player_name_dis = tk.Label(self.inferior_status_frame, text = "Username: "+self.player_name)
        self.player_name_dis.pack(side = "top", fill= "x")

        self.player_money_dis = tk.Label(self.inferior_status_frame, text="Money: " + str(dicto[self.player_name]["money"]))
        self.player_money_dis.pack(side="top", fill="x")

        # do something like drop down menu for props and also find something for handling chance

    def dis_stat_update(self):
        # update whatever changes happen
        pass






