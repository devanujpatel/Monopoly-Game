# necessary for non-overlapping token display

import tkinter as tk

sticky_id = {"token1": "N", "token2": "S", "token3": "w", "token4": "e", "token5": "NE", "token6": "NW", "token7": "SW",
             "token8": "se"}

def step_3(main_frame,status_frame,properties_dicto, n_players, playing_tokens, colors,sf_width, sf_height,row_coordinates,column_coordinates,place_num):
    import initialising_everything

    class token:
        def __init__(self, token_str, player_str,dis_str):
            self.dis_str = dis_str
            self.token_str = token_str
            self.player_str = player_str

        def my_special_init(self):
            print(self.token_str,colors[self.token_str])
            self.token_id = tk.Label(main_frame,text=self.dis_str,bg=colors[self.token_str],
                                 highlightbackground="black", highlightthickness=1)
            self.token_id.grid(row=10,column = 10,sticky = sticky_id[self.token_str])
            self.dicto = {self.token_str: {"position": 0, "row": row_coordinates["go box"], "column": column_coordinates["go box"]}}
            self.dicto_2 = {self.player_str: {"token_id": self.token_id, "token_str": self.token_str, "money": 1500}}
            initialising_everything.master_dictionary.update(self.dicto)
            initialising_everything.master_dictionary.update(self.dicto_2)
            self.token_id.grid(row=10, column=10, sticky=sticky_id[self.token_str])

        def token_move(self, position):
            initialising_everything.master_dictionary[self.token_str]["position"] = position
            p = place_num[position]
            row = row_coordinates[p]
            column = column_coordinates[p]
            self.token_id.grid_forget()
            self.token_id.grid(row=row, column=column, sticky=sticky_id[self.token_str])
            properties_dicto[position].show_details()

    t1 = token("token1", "player1","T1")
    t2 = token("token2", "player2","T2")
    t3 = token("token3", "player3","T3")
    t4 = token("token4", "player4","T4")
    t5 = token("token5", "player5","T5")
    t6 = token("token6", "player6","T6")
    t7 = token("token7", "player7","T7")
    t8 = token("token8", "player8","T8")

    t1.my_special_init()
    t2.my_special_init()

    if "token3" in playing_tokens:
        t3.my_special_init()
    if "token4" in playing_tokens:
        t4.my_special_init()
    if "token5" in playing_tokens:
        t5.my_special_init()
    if "token6" in playing_tokens:
        t6.my_special_init()
    if "token7" in playing_tokens:
        t7.my_special_init()
    if "token8" in playing_tokens:
        t8.my_special_init()

    token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]

    for i in range(n_players):
        initialising_everything.playing_token_obj_id.append(token_objs[i])

    import status_of_player
    status_of_player.step_4(status_frame, sf_width, sf_height, n_players, playing_tokens, colors)

