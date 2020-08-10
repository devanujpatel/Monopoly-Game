import tkinter as tk

root = tk.Tk()

def empty_dictionaries():
    global player_props,tokens,player_pos
    player_props={}
    tokens = {}
    player_pos={}

empty_dictionaries()

entry = tk.Entry(root)
entry.pack()

def working_lists():
    global all_tokens, playing_tokens

    all_tokens = []
    num = 1
    for t in range(8):
        tok = "token" + str(num)
        all_tokens.append(tok)
        num += 1

    playing_tokens = []

    num = 1
    for i in range(n_players):
        tok =  "token" + str(num)
        playing_tokens.append(tok)
        num += 1

def initializing():

    global n_players,show_button
    n_players = entry.get()
    n_players= int(n_players)

    if n_players > 8:
       pass

    num = 1
    for n in range(n_players):

        token_name = "token"+str(num)
        tokens.update({token_name:""})

        player_name = "player"+str(num)
        player_props.update({player_name:""})

        player_pos.update({player_name:""})

        num+=1

    print(tokens)
    print(player_props)
    print(player_pos)

    root.destroy()
    working_lists()
    #print(playing_tokens)

play_button = tk.Button(text='PLAY!', command=initializing)
play_button.pack()

root.mainloop()

"""def move_token():
    global token1,update_tokens

    for a in myplaces:
        if position == myplace_num[a]:
            update_tokens = True
"""
play = True
while play:
    from Token_movement import *
    if update_tokens == True:
        pass
