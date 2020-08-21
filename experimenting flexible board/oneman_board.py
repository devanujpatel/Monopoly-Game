import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen


root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

calc_height = height - 160
calc_width = width - 280
horizontal_lane_height = calc_height/9
horizontal_lane_width = calc_width/9.5
horizontal_lane_height = int(horizontal_lane_height/7)
horizontal_lane_width = int(horizontal_lane_width/7)

vertical_height = 120
vertical_width = 480
verti_height = height - 120
verti_width = width - 280

vertical_lane_height = vertical_height/5.5
verical_lane_width = vertical_width/4.5
vertical_lane_height = int(vertical_lane_height/5.5)
vertical_lane_width = int(verical_lane_width/4.4)
#upper lane

free_parking = tkinter.Label(root,text="Free Parking",font=(1),borderwidth=4,relief="ridge", width=horizontal_lane_width,height=horizontal_lane_height,bg = "yellow",fg= "blue", highlightbackground="black").grid(row=1,column=0)

kentucky = tkinter.Label(root,text="kentucky Avenue \n $10 ",borderwidth=2,relief="sunken",width=horizontal_lane_width,height=horizontal_lane_height,bg = "red",highlightbackground="black").grid(row=1,column=1)

chance_2 = tkinter.Label(root,text="Chance_2",borderwidth=2,relief="sunken",width=horizontal_lane_width,height=horizontal_lane_height,bg = "white", highlightbackground="black").grid(row=1,column=2)

indiana = tkinter.Label(root, text="Indiana Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "red", highlightbackground="black").grid(row=1, column=3)

illinois = tkinter.Label(root, text="Illinois Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Red", highlightbackground="black").grid(row=1, column=4)

b_and_o_railroad = tkinter.Label(root, text='b_and_o_railroad \n $12',borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue", highlightbackground="black").grid(row=1, column=5)

atlantic = tkinter.Label(root, text='Atlantic Avenue \n $12',borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "yellow", highlightbackground="black").grid(row=1, column=6)

venitnor= tkinter.Label(root, text='Venitnor Avenue \n $12',borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "yellow", highlightbackground="black").grid(row=1, column=7)

water_works= tkinter.Label(root, text='water works \n $12',borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "white", highlightbackground="black").grid(row=1, column=8)

marvin_gardens= tkinter.Label(root, text='Marvin Gardens \n $12',borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "yellow", highlightbackground="black").grid(row=1, column=9)

go_to_jail = tkinter.Label(root,text="Go To Jail",font=(1),borderwidth=4,relief="ridge", width=horizontal_lane_width,height=horizontal_lane_height,bg = "light green", highlightbackground="black").grid(row=1,column=10)

#lower lane

go_box = tkinter.Label(root, text="Go Box",font=(1),borderwidth=4,relief="ridge", width=horizontal_lane_width, height=horizontal_lane_height,bg = "yellow", highlightbackground="black").grid(row=11, column=10)

Mediterenian_Avenue = tkinter.Label(root, text="Mediterenian Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "brown", highlightbackground="black").grid(row=11, column=9)

Community_chest1 = tkinter.Label(root, text="Community chest",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "white").grid(row=11, column=8)

Baltic_Avenue = tkinter.Label(root, text="Baltic Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "brown").grid(row=11, column=7)

Income_tax = tkinter.Label(root, text="Income Tax",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue").grid(row=11, column=6)

Railway1 = tkinter.Label(root, text="Reading Railrod \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue").grid(row=11, column=5)

Orental_Avenue = tkinter.Label(root, text="Orental Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "light blue").grid(row=11, column=4)

Chance1 = tkinter.Label(root, text="Chance1",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "white").grid(row=11, column=3)

Vermount_Avenue = tkinter.Label(root, text="Vermount Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "light blue").grid(row=11, column=2)

Connectinut_Avenue = tkinter.Label(root, text="Connectinut Avenue \n $12",borderwidth=2,relief="sunken", width=horizontal_lane_width, height=horizontal_lane_height,bg = "light blue").grid(row=11, column=1)

Just_visiting = tkinter.Label(root, text="Just Visiting",font=(1),borderwidth=4,relief="ridge", width=horizontal_lane_width, height=horizontal_lane_height,bg = "orange").grid(row=11, column=0)

#right column

Pacific_Avenue = tkinter.Label(root, text="Pacific Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "green").grid(row=2, column=10)

North_Carolina_Avenue = tkinter.Label(root, text="North Carolina Avenue \n $13",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "green").grid(row=3, column=10)

Community_chest3 = tkinter.Label(root, text="Community Chest",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "white").grid(row=4, column=10)

Pensylvania_Avenue = tkinter.Label(root, text="Pensylvania Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "green").grid(row=5, column=10)

Railway4 = tkinter.Label(root, text="Short Line \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "Blue").grid(row=6, column=10)

Chance3 = tkinter.Label(root, text="Chance",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "white").grid(row=7, column=10)

Park_Lane = tkinter.Label(root, text="Park Lane \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "dark Blue",fg="red").grid(row=8, column=10)

Luxury_Tax = tkinter.Label(root, text="Luxury Tax",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "red").grid(row=9, column=10)

Boardwalk = tkinter.Label(root, text="Boardwalk \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "dark Blue",fg="red").grid(row=10, column=10)

#left column

New_york_Avenue = tkinter.Label(root, text="New york Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "orange").grid(row=2 , column=0)

Tenesse_Avenue = tkinter.Label(root, text="Tenesse_Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "orange").grid(row=3, column=0)

Community_chest2 = tkinter.Label(root, text="Community Chest",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "white").grid(row=4, column=0)

ST_James_Place = tkinter.Label(root, text="ST. James Place \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "orange").grid(row=5, column=0)

Railway2 = tkinter.Label(root, text="Pensylvania Railroad\n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "Blue").grid(row=6, column=0)

Virginia_Avenue = tkinter.Label(root, text="Virginia Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "pink").grid(row=7, column=0)

States_Avenue = tkinter.Label(root, text="States Avenue \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "pink").grid(row=8, column=0)

Electric_company = tkinter.Label(root, text="Electric_company \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "white").grid(row=9, column=0)

ST_Charles_Place = tkinter.Label(root, text="ST. Charles Place \n $12",borderwidth=2,relief="sunken", width=vertical_lane_width, height=vertical_lane_height,bg = "pink").grid(row=10 , column=0)



root.mainloop()

# 1366 768