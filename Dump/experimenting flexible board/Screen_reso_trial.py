import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

calc_height = height - 160
calc_width = width - 280
horizontal_lane_height = calc_height/9
horizontal_lane_width = calc_width/9
# robl;ox sd
import tkinter.font as tkfont
font = tkfont.Font(family="Consolas", size=10, weight="normal")
m_len = font.measure("0")

horizontal_lane_height = int(horizontal_lane_height/m_len)
horizontal_lane_width = int(horizontal_lane_width/m_len)
col_hor = 0
free_parking = tkinter.Label(root,text="Free Parking",width=int(140/m_len),height=int(80/m_len),bg = "orange").grid(row=1,column=col_hor)
col_hor += 1
kentucky = tkinter.Label(root,text="kentucky Avenue",width=horizontal_lane_width,height=horizontal_lane_height,bg = "LightSteelBlue1").grid(row=1,column=col_hor)
col_hor += 1
chance_2 = tkinter.Label(root,text="Chance_2",width=horizontal_lane_width,height=horizontal_lane_height,bg = "orange").grid(row=1,column=col_hor)
col_hor += 1
indiana = tkinter.Label(root, text="Indiana Avenue", width=horizontal_lane_width, height=horizontal_lane_height,bg = "LightSteelBlue1").grid(row=1, column=col_hor)
col_hor += 1
illinois = tkinter.Label(root, text="Illinois Avenue", width=horizontal_lane_width, height=horizontal_lane_height,bg = "orange").grid(row=1, column=col_hor)
col_hor += 1
b_and_o_railroad = tkinter.Label(root, text='b_and_o_railroad', width=horizontal_lane_width, height=horizontal_lane_height,bg = "LightSteelBlue1").grid(row=1, column=col_hor)
col_hor += 1
atlantic = tkinter.Label(root, text='Atlantic Avenue', width=horizontal_lane_width, height=horizontal_lane_height,bg = "orange").grid(row=1, column=col_hor)
col_hor += 1
venitnor= tkinter.Label(root, text='Venitnor Avenue', width=horizontal_lane_width, height=horizontal_lane_height,bg = "LightSteelBlue1").grid(row=1, column=col_hor)
col_hor += 1
water_works= tkinter.Label(root, text='water works', width=horizontal_lane_width, height=horizontal_lane_height,bg = "orange").grid(row=1, column=col_hor)
col_hor += 1
marvin_gardens= tkinter.Label(root, text='Marvin Gardens', width=horizontal_lane_width, height=horizontal_lane_height,bg = "LightSteelBlue1").grid(row=1, column=col_hor)
col_hor += 1
go_to_jail = tkinter.Label(root,text="Go To Jail",width=int(140/m_len),height=int(80/m_len),bg = "orange").grid(row=1,column=col_hor)


tkinter.Label(root, text='Marvin Gardens', width = width, height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=2, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=3, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=4, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=5, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=6, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=7, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=8, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=9, column=11)

tkinter.Label(root, text='Marvin Gardens', width = horizontal_lane_height,height = horizontal_lane_width,bg = "LightSteelBlue1").grid(row=10, column=11)


root.mainloop()

# 1366 768