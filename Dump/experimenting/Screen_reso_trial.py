import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

calc_height = height - 160
calc_width = width - 280
horizontal_lane_height = calc_height/9
horizontal_lane_width = calc_width/9
horizontal_lane_height = int(horizontal_lane_height/7)
horizontal_lane_width = int(horizontal_lane_width/7)
col_hor = 0
free_parking = tkinter.Label(root,text="Free Parking",width=horizontal_lane_width,height=horizontal_lane_height,bg = "Red").grid(row=1,column=col_hor)
col_hor += 1
kentucky = tkinter.Label(root,text="kentucky Avenue",width=horizontal_lane_width,height=horizontal_lane_height,bg = "Blue").grid(row=1,column=col_hor)
col_hor += 1
chance_2 = tkinter.Label(root,text="Chance_2",width=horizontal_lane_width,height=horizontal_lane_height,bg = "Red").grid(row=1,column=col_hor)
col_hor += 1
indiana = tkinter.Label(root, text="Indiana Avenue", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue").grid(row=1, column=col_hor)
col_hor += 1
illinois = tkinter.Label(root, text="Illinois Avenue", width=horizontal_lane_width, height=horizontal_lane_height,bg = "Red").grid(row=1, column=col_hor)
col_hor += 1
b_and_o_railroad = tkinter.Label(root, text='b_and_o_railroad', width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue").grid(row=1, column=col_hor)
col_hor += 1
atlantic = tkinter.Label(root, text='Atlantic Avenue', width=horizontal_lane_width, height=horizontal_lane_height,bg = "Red").grid(row=1, column=col_hor)
col_hor += 1
venitnor= tkinter.Label(root, text='Venitnor Avenue', width=horizontal_lane_width, height=horizontal_lane_height,bg = "Blue").grid(row=1, column=col_hor)
col_hor += 1
water_works= tkinter.Label(root, text='water works', width=horizontal_lane_width, height=horizontal_lane_height,bg = "Red").grid(row=1, column=col_hor)
col_hor += 1
marvin_gardens= tkinter.Label(root, text='Marvin Gardens', width=horizontal_lane_width, height=horizontal_lane_height,bg = "Red").grid(row=1, column=col_hor)
col_hor += 1
go_to_jail = tkinter.Label(root,text="Go To Jail",width=horizontal_lane_width,height=horizontal_lane_height,bg = "Red").grid(row=1,column=col_hor)

root.mainloop()

# 1366 768