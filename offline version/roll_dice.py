"""import tkinter as tk


def step_5(main_frame, font1, n_players, properties_dicto):
    import initialising_everything as it
    import random
    class roll_dice_class():

        def __init__(self):

            global roll_dice_d
            roll_dice_d = tk.Button(main_frame, text="Roll Dice!", bg="orange", font=font1,
                                    command=lambda: self.virtual_dice())
            roll_dice_d.grid(row=6, column=6)

        def virtual_dice(self):
            roll_dice_d.grid_forget()
            self.token_str = it.playing_tokens[it.chance]
            self.token_id = it.playing_token_obj_id[it.chance]

            dice_roll1 = random.randint(1, 6)
            dice_roll2 = random.randint(1, 6)
            dice_roll = dice_roll1 + dice_roll2
            show_dice = tk.StringVar()
            label_dice = "Dice Roll = " + str(dice_roll)
            show_dice.set(label_dice)
            tk.Label(main_frame, textvariable=show_dice, bg="green", fg="orange", width=12, height=2).grid(row=7,
                                                                                                           column=5)

            position = it.master_dictionary[self.token_str]["position"]
            # old_position = it.master_dictionary[self.token_str]["old position"]
            position += dice_roll

            if position >= 40:
                position -= 40

            self.token_id.token_move(position)

            global end_turn
            end_turn = tk.Button(main_frame, text="End Turn!", font=font1, command=lambda: self.end_turn_clicked())
            end_turn.grid(row=6, column=6)

        def end_turn_clicked(self):

            position = it.master_dictionary[it.playing_tokens[it.chance]]["position"]
            properties_dicto[position].info_box1.grid_forget()
            properties_dicto[position].info_box2.grid_forget()
            properties_dicto[position].buy_button.grid_forget()
            # stat_objs[it.chance].normal_relief()

            it.chance += 1
            max_chance = n_players

            # [it.chance].raise_relief()

            if it.chance == max_chance:
                it.chance = 0

            end_turn.grid_forget()
            roll_dice_d.grid(row=6, column=6)

    rollie_pollie = roll_dice_class()

"""

