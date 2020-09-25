# this module will be handling the main game and starts with defining the main window and asking n_players

import tkinter as tk
import initialising_everything

container = tk.Tk()
width = container.winfo_screenwidth()  # width of screen
height = container.winfo_screenheight()  # height of screen

container.winfo_toplevel().geometry("%dx%d%+d%+d" % (width, height, 0, 0))

# think of this frame as the intro frame or page-one
start_frame= tk.Frame(container, width=width, height=height)
start_frame.grid(row=0, column=0, sticky="nsew")

font1=("Courier", 13)

entry = tk.Entry(start_frame)
entry.place(relx=0.4, rely=0.4)
play_button = tk.Button(start_frame, text="Play!",font=font1, command=lambda: play_but_clicked())
play_button.place(relx=0.42, rely=0.44)

def play_but_clicked():
    n_players = entry.get()


    #if n_players in initialising_everything.n_player_list:
    n_players = int(n_players)


    for num in range(int(n_players)):
        tok = "token" + str(num + 1)
        initialising_everything.playing_tokens.append(tok)
        pal = "player" + str(num + 1)
        initialising_everything.player_chances.append(pal)
        initialising_everything.chances.update({tok: num})
    entry.place_forget()
    play_button.place_forget()

    import class_ask_info
    class_ask_info.step_1(container, font1, start_frame, initialising_everything.player_chances,
                          initialising_everything.playing_tokens,
                          n_players, initialising_everything.asf_x, initialising_everything.asf_y, initialising_everything.chance)

container.mainloop()
    #else:
        #print("somethings wrong")



