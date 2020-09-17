import  gui_monopoly_fnc, play_game
from status_of_player import Status_of_player
from class_token import token


def make_objs():
    t1 = token(gui_monopoly_fnc.token1, "token1", "player1")
    t2 = token(gui_monopoly_fnc.token2, "token2", "player2")
    t3 = token(gui_monopoly_fnc.token3, "token3", "player3")
    t4 = token(gui_monopoly_fnc.token4, "token4", "player4")
    t5 = token(gui_monopoly_fnc.token5, "token5", "player5")
    t6 = token(gui_monopoly_fnc.token6, "token6", "player6")
    t7 = token(gui_monopoly_fnc.token7, "token7", "player7")
    t8 = token(gui_monopoly_fnc.token8, "token8", "player8")

    t1.my_special_init()
    t2.my_special_init()

    stat1 = Status_of_player("token1", play_game.play_but_clicked().player_names["player1"])
    stat2 = Status_of_player("token2", play_game.play_but_clicked().player_names["player2"])
    stat3 = Status_of_player("token3", play_game.play_but_clicked().player_names["player3"])
    stat4 = Status_of_player("token4", play_game.play_but_clicked().player_names["player4"])
    stat5 = Status_of_player("token5", play_game.play_but_clicked().player_names["player5"])
    stat6 = Status_of_player("token6", play_game.play_but_clicked().player_names["player6"])
    stat7 = Status_of_player("token7", play_game.play_but_clicked().player_names["player7"])
    stat8 = Status_of_player("token8", play_game.play_but_clicked().player_names["player8"])

    stat1.display()
    stat1.raise_relief()
    stat2.display()

    if "token3" in play_game.play_but_clicked().playing_tokens:
        t3.my_special_init()
        stat3.display()
    if "token4" in play_game.play_but_clicked().playing_tokens:
        t4.my_special_init()
        stat4.display()
    if "token5" in play_game.play_but_clicked().playing_tokens:
        t5.my_special_init()
        stat5.display()
    if "token6" in play_game.play_but_clicked().playing_tokens:
        t6.my_special_init()
        stat6.display()
    if "token7" in play_game.play_but_clicked().playing_tokens:
        t7.my_special_init()
        stat7.display()
    if "token8" in play_game.play_but_clicked().playing_tokens:
        t8.my_special_init()
        stat8.display()
    global stat_objs
    # stat_objs = [stat1, stat2,stat3, stat4,stat5, stat6,stat7, stat8]
    token_objs = [t1, t2, t3, t4, t5, t6, t7, t8]

    for i in range(play_game.play_but_clicked().n_players):
        play_game.play_but_clicked().playing_token_obj_id.append(token_objs[i])
