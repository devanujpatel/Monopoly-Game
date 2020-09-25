import tkinter as tk

root = tk.Tk()

def empty_dictionary():
    global player_props,tokens,player_pos
    player_props={}
    tokens = {}
    player_pos={}

empty_dictionary()
entry = tk.Entry(root)
entry.pack()

def initializing():

    n_players= entry.get()
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
    print(tokens,"\t",player_props,"\t",player_pos)

play_button = tk.Button(text='PLAY!', command=initializing)
play_button.pack()

root.mainloop()