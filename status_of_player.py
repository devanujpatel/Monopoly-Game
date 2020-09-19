import tkinter as tk
from initialising_everything import chance,chances, player_names

def step_4(status_frame,sf_width,sf_height,n_players,playing_tokens, colors):
    class Status_of_player:
        def __init__(self, token_str, player_str):
            self.token_str = token_str
            self.player_str = player_str
        def display(self):
            self.inferior_status_frame = tk.LabelFrame(status_frame, text=self.player_str, bg=colors[self.token_str], relief="flat",
                                                       width=sf_width / n_players, height=sf_height, font=("white",11), bd=7)

            if chance ==  chances[self.token_str]:
                self.inferior_status_frame["relief"] = "raised"

            self.inferior_status_frame.pack(side="left")

        def raise_relief(self):
            self.inferior_status_frame["relief"] = "raised"

        def normal_relief(self):
            self.inferior_status_frame["relief"] = "flat"

    global stat1,stat2,stat3,stat4,stat5,stat6,stat7,stat8
    stat1 = Status_of_player("token1", player_names["player1"])
    stat2 = Status_of_player("token2", player_names["player2"])
    stat3 = Status_of_player("token3", player_names["player3"])
    stat4 = Status_of_player("token4", player_names["player4"])
    stat5 = Status_of_player("token5", player_names["player5"])
    stat6 = Status_of_player("token6", player_names["player6"])
    stat7 = Status_of_player("token7", player_names["player7"])
    stat8 = Status_of_player("token8", player_names["player8"])

    stat1.display()
    stat1.raise_relief()
    stat2.display()

    if "token3" in playing_tokens:
        stat3.display()
    if "token4" in playing_tokens:
        stat4.display()
    if "token5" in playing_tokens:
        stat5.display()
    if "token6" in playing_tokens:
        stat6.display()
    if "token7" in playing_tokens:
        stat7.display()
    if "token8" in playing_tokens:
        stat8.display()

    global stat_objs
    stat_objs = [stat1, stat2,stat3, stat4,stat5, stat6,stat7, stat8]