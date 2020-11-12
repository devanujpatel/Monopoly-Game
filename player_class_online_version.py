import tkinter as tk
import time
font = ("Courier", 12)
class Player:
    # this class is meant only for display updates
    def __init__(self, main_frame_para, stat_box_para, dicto_para, name):
        # this is the same main frame from client file code
        global main_frame, stat_box, data_holder
        data_holder = dicto_para
        stat_box = stat_box_para
        main_frame = main_frame_para
        self.name = name
        self.sticky = data_holder["token dir"][self.name]

        self.dis_token()

    def dis_token(self):
        self.token = tk.Label(main_frame, text="T" + str(data_holder["player chances"][self.name] + 1),
                              bg=data_holder["game info"][self.name]["color"], width=3, height=2)
        self.token.grid(row=10, column=10, sticky=self.sticky)

    def update_position(self, row_coord, col_coord, place_num, old_pos, new_pos, place_id, prop_obj_id, chance, username, client):
        print("new pos old pos",new_pos, old_pos)
        destination = place_num[new_pos]
        dest_row = row_coord[destination]
        dest_col = col_coord[destination]
        print("dest",dest_row, dest_col)

        showcase_num = 0
        show_dice = tk.StringVar()
        show_dice.set(str(showcase_num))

        self.rd_label = tk.Label(main_frame, textvariable=show_dice, bg="green", fg="orange", width=12, height=2, font = ("Courier", 11))
        self.rd_label.grid(row=7, column=5)

        while True:
            self.token.grid_forget()
            next_spot = place_num[old_pos+1]
            print("next spot",next_spot)
            row = row_coord[next_spot]
            col = col_coord[next_spot]

            print("current position",row,col)
            time.sleep(0.3)
            self.token.grid(row = row, column = col, sticky = self.sticky)
            showcase_num += 1
            show_dice.set(str(showcase_num))
            time.sleep(1)
            if dest_col == col and dest_row == row:
                show_dice.set("Dice Roll: "+str(showcase_num))
                prop_obj_id[new_pos].playerOnSite(chance,username,client)
                break

            old_pos = place_id[next_spot]
            print("round completed")




# ignore
'''    def dis_token(self):
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
        pass'''
