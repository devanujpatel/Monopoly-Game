import tkinter as tk
from tkinter import ttk
import time, pickle
from prop_class_for_online_version import prop_info

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

    def update_data_holder(self, data_holder_para):
        global data_holder
        data_holder = data_holder_para
        print("IN UPDATE DATA HOLDER",data_holder)
        
    def update_position(self, row_coord, col_coord, place_num, old_pos, new_pos, place_id, prop_obj_id, chance,
                        player_name, client_para, rd_obj):
        global client
        client = client_para
        print("new pos old pos", new_pos, old_pos)
        destination = place_num[new_pos]
        dest_row = row_coord[destination]
        dest_col = col_coord[destination]
        print("dest", dest_row, dest_col)

        showcase_num = 0
        show_dice = tk.StringVar()
        show_dice.set(str(showcase_num))

        self.rd_label = tk.Label(main_frame, textvariable=show_dice, bg="green", fg="orange", width=12, height=2,
                                 font=("Courier", 11))
        self.rd_label.grid(row=7, column=5)

        while True:
            self.token.grid_forget()
            next_spot = place_num[old_pos + 1]
            print("next spot", next_spot)
            row = row_coord[next_spot]
            col = col_coord[next_spot]

            print("current position", row, col)
            # time.sleep(0.3)
            self.token.grid(row=row, column=col, sticky=self.sticky)
            showcase_num += 1
            show_dice.set(str(showcase_num))
            # time.sleep(0.4)
            if dest_col == col and dest_row == row:
                show_dice.set("Dice Roll: " + str(showcase_num))
                main_frame.after(3600*2, lambda : self.rd_label.grid_forget())
                print("passing data holder",data_holder)
                prop_obj_id[new_pos].playerOnSite(chance, player_name, client, rd_obj, data_holder)
                break

            old_pos = place_id[next_spot]
            print("round completed")

    def status_frame_display(self, sf_width, sf_height):
        self.sf_width = int(sf_width)
        self.sf_height = int(sf_height)
        # display smaller frame inside our stat box
        self.inferior_status_frame = tk.Label(stat_box, bg="tomato1", relief="flat", font=("white", 1),
                                              width=int(sf_width / len(data_holder["players list"])),
                                              height=self.sf_height)

        self.inferior_status_frame = tk.Label(stat_box, bg="tomato1", relief="flat",
                                              width=int(sf_width / len(data_holder["players list"])),
                                              height=self.sf_height - 10)

        self.stat_notebook = ttk.Notebook(self.inferior_status_frame,
                                          width=int(self.sf_width / len(data_holder["players list"])),
                                          height=self.sf_height)
        self.stat_notebook = ttk.Notebook(self.inferior_status_frame,
                                          width=int(self.sf_width / len(data_holder["players list"])),
                                          height=self.sf_height - 8)
        self.stat_notebook.pack()

        self.details_frame = tk.Frame(self.stat_notebook, bg="light blue")
        self.properties_frame = tk.Frame(self.stat_notebook, bg="light blue")

        self.proptree = ttk.Treeview(self.properties_frame, selectmode="none", height=self.sf_height)
        self.proptree = ttk.Treeview(self.properties_frame, selectmode="none", height=self.sf_height - 8)
        self.proptree.pack(fill="x")
        self.proptree["columns"] = ("Property Name", "Price", "Houses", "Current Rent")
        self.proptree.column("#0", width=0)
        self.proptree.column("Property Name", width=60, minwidth=50, anchor="w")
        self.proptree.column("Price", width=30, minwidth=20, anchor="w")
        self.proptree.column("Houses", width=30, minwidth=10, anchor="w")
        self.proptree.column("Current Rent", width=20, minwidth=10, anchor="w")
        # create headings
        self.proptree.heading("#0", text="")
        self.proptree.heading("Property Name", text="Prop. Name", anchor="w")
        self.proptree.heading("Price", text="Price", anchor="w")
        self.proptree.heading("Houses", text="Houses", anchor="w")
        self.proptree.heading("Current Rent", text="Current Rent", anchor="w")

        self.stat_notebook.add(self.details_frame, text=self.name + "'s Stats")
        self.stat_notebook.add(self.properties_frame, text=self.name + "'s Properties")

        self.money_var = tk.StringVar()
        self.money_var.set(data_holder["game info"][self.name]["money"])

        self.num_props = tk.StringVar()
        self.num_props.set(str(len(data_holder["game info"][self.name]["properties"])))

        self.chance_var = tk.StringVar()
        self.chance_var.set(data_holder["player chances"][self.name])

        self.name_label = tk.StringVar()
        self.name_label.set(self.name)

        self.player_name_label = tk.Label(self.details_frame, text="Name: " + self.name_label.get())
        self.player_name_label.pack(pady=5, fill="x")

        self.money_label = tk.Label(self.details_frame, text="Money: " + self.money_var.get())
        self.money_label = tk.Label(self.details_frame,
                                    text="Money: " + str(data_holder["game info"][self.name]["money"]))
        self.money_label.pack(pady=5, fill="x")

        self.prop_num_label = tk.Label(self.details_frame, text="Properties in hand: " + self.num_props.get())
        self.prop_num_label = tk.Label(self.details_frame, text="Properties in hand: " + str(
            len(data_holder["game info"][self.name]["properties"])))
        self.prop_num_label.pack(pady=5, fill="x")

        self.chance_label = tk.Label(self.details_frame, text="Chance: " + self.chance_var.get())
        self.chance_label = tk.Label(self.details_frame,
                                     text="Chance: " + str(data_holder["player chances"][self.name]))
        self.chance_label.pack(pady=5, fill="x")

        self.inferior_status_frame.pack(side="left")

        #self.trade_tab()

    def trade_tab(self):
        self.trade_frame = tk.Frame(self.stat_notebook, width=int(self.sf_width / len(data_holder["players list"])),
                                    height=self.sf_height - 10)
        self.trade_with = ttk.Combobox(self.trade_frame, width=27)
        self.trade_with["values"] = data_holder["players list"]
        self.trade_with.bind("<<ComboboxSelected>>", self.trade_with_select)
        self.trade_with.pack()

        self.type_of_trade = ttk.Combobox(self.trade_with, width=27)
        self.type_of_trade["values"] = ["only property", "money and property"]
        self.type_of_trade.bind("<<ComboboxSelected>>", self.trade_type_select)
        self.type_of_trade.pack()

        self.okay = tk.Button(self.trade_frame, text="Okay", command=lambda: self.okay_btn_clk())

    def okay_btn_clk(self):
        self.trade_with.pack_forget()
        self.type_of_trade.pack_forget()
        self.trading_with = tk.Label(self.trade_frame, text="You are trying to trade with " + self.trade_player,
                                     font=font)
        self.trading_with.pack()
        
        self.type_of_trading = tk.Label(self.trade_frame, text = "Trade Type: "+self.trade_type, font=font)
        self.type_of_trading.pack()

        self.revert_btn = tk.Button(self.trade_frame, text = "Change Options", commanda=lambda:self.trade_tab())
        self.revert_btn.pack()

        self.okay_btn = tk.Button(self.trade_frame, text = "Let's Trade", command=lambda:self.go_trade())
        self.okay_btn.pack()

    def go_trade(self):

        if self.trade_type == "only property":
            self.only_prop_trade()

        else:
            self.m_and_p_trade()

    def only_prop_trade(self):
        self.prop_box_owned = ttk.Combobox(self.trade_frame, values = data_holder["game info"][self.name]["properties"].keys())
        self.prop_box_owned.bind("<<ComboboxSelected>>", self.prop_box_owned_clk())
        self.prop_box_owned.pack()

        self.prop_box_theirs = ttk.Combobox(self.trade_frame, values = data_holder["game info"][self.trade_with]["properties"].keys())
        self.prop_box_theirs.bind("<<ComboboxSelected>>", self.prop_box_theirs_clk())
        self.prop_box_owned.pack()

        self.prop_trade_btn = tk.Button(self.trade_frame, text = "Propose Trade", command=lambda:self.prop_trade_okay_btn())

    def m_and_p_trade(self):
        pass

    def prop_box_theirs_clk(self):
        self.want_prop = self.prop_box_theirs.get()

    def prop_box_owned_clk(self):
        self.give_prop = self.prop_box_owned.get()

    def prop_trade_okay_btn(self):
        self.prop_box_owned.pack_forget()
        self.prop_box_theirs.pack_forget()
        self.prop_trade_btn.pack_forget()

        self.proposing_trade_l = tk.Label(self.trade_frame, text = f"Proposing Trade \n Waiting for confirmation of {self.trade_with} \n to accept a {self.trade_type}. \n {self.name} want to give {self.give_prop} in return of {self.want_prop}.")

        # tell server we want to trade
        # only one trade can take place at a time
        # so server will block all other trade requests
        client.send(pickle.dumps((self.name, "trade proposal", self.trade_type, self.trade_with, self.give_prop, self.want_prop)))

        # else all will be taken care of by the client file code and the server

    def trade_type_select(self):
        self.trade_type = self.type_of_trade.get()

    def trade_with_select(self):
        self.trade_player = self.trade_with.get()

    def watch_trade(self):
        pass
    def recv_trade_request(self):
        pass
    def trade_finalised(self):
        pass

    def trade_declined(self):
        pass

    def property_remove(self):
        pass

    def property_update(self, update):
        self.proptree.insert(parent="", index="end", text="",
                             values=(update[3], str(prop_info[update[3]]["price"]), str(prop_info[update[3]]["houses"]),
                                     str(prop_info[update[3]]["current rent"])))

    def player_left(self, data_holder, created_objs):
        self.token.grid_forget()
        self.inferior_status_frame.grid_forget()
        for player in created_objs:
            player.inferior_status_frame["width"] = int(self.sf_width/len(data_holder["players list"]))



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
        self.player_name_dis = tk.Label(self.inferior_status_frame, text = "player_name: "+self.player_name)
        self.player_name_dis.pack(side = "top", fill= "x")

        self.player_money_dis = tk.Label(self.inferior_status_frame, text="Money: " + str(dicto[self.player_name]["money"]))
        self.player_money_dis.pack(side="top", fill="x")

        # do something like drop down menu for props and also find something for handling chance

    def dis_stat_update(self):
        # update whatever changes happen
        pass

                self.details = ttk.Treeview(self.inferior_status_frame, selectmode="none")
        self.details.pack()
        self.details["columns"] = ("Name", "Chance", "Money", "No. of Properties")
        self.details.column("#0", width=0)
        self.details.column("Name", width=90, minwidth=50, anchor="w")
        self.details.column("Chance", width=20, minwidth=20, anchor="w")
        self.details.column("Money", width=90, minwidth=50, anchor="w")
        self.details.column("No. of Properties", width=90, minwidth=50, anchor="w")
        # create headings
        self.details.heading("#0", text="")
        self.details.heading("Name", text="Player Name", anchor="w")
        self.details.heading("Chance", text="Chance", anchor="w")
        self.details.heading("Money", text="Money", anchor="w")
        self.details.heading("No. of Properties", text="No. of Properties", anchor="w")

        self.money_var = tk.StringVar()
        self.money_var.set(data_holder["game info"][self.name]["money"])

        self.num_props = tk.StringVar()
        self.num_props.set(len(data_holder["game info"][self.name]["properties"]))

        self.details.insert(parent="", index="end", text="",
                           values=(self.name, str(data_holder["player chances"][self.name]) ,self.money_var, self.num_props))

        #self.money_var = tk.StringVar()
        #self.money_var.set(data_holder["game info"][self.name]["money"])

        #self.num_props = tk.StringVar()
        #self.num_props.set(str(len(data_holder["game info"][self.name]["properties"])))

        #self.chance_var = tk.StringVar()
        #self.chance_var.set(data_holder["player chances"][self.name])

        '''
