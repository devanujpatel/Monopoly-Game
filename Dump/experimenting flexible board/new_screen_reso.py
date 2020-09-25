import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

import tkinter.font as tkfont
font = tkfont.Font(family="Consolas", size=10, weight="normal")
m_len = font.measure("0")

height = height/m_len
width = width/m_len

width = int(width/9)
height = int(height/9)




free_parking = tkinter.Label(root,width=width,height=height,bg="orange").grid(row=0,column=0)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=1)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=2)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=3)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=4)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=5)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=6)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=7)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=8)
tkinter.Label(root,  width = width, height = height,bg = "LightSteelBlue1").grid(row=0, column=9)
go_jail = tkinter.Label(root,width=width,height=height,bg="purple").grid(row=0,column=10)

tkinter.Label(root, width=width, height=height, bg="blue").grid(row=1, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=2, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=3, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=4, column=0)
tkinter.Label(root, width=width, height=height, bg='green').grid(row=5, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=6, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=7, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=8, column=0)
tkinter.Label(root, width=width, height=height, bg="purple").grid(row=9, column=0)


root.mainloop()

