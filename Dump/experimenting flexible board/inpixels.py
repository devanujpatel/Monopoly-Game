import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

root.geometry("%dx%d%+d%+d" % (width, height, 0 ,0))

import tkinter.font as tkfont
font = tkfont.Font(family="Consolas", size=10, weight="normal")

m_len = font.measure("0")

height = int(height/m_len)
width = int(width/m_len)

width = int(width / 11)
height = int((height / 11))
ratio = width/height
height = int((height / ratio))
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

width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight()# height of screen

m_len = font.measure("0")
height = int(height/m_len)
width = int(width/m_len)

width = int(width / 11)
height = int((height / 11))
ratio = width/height
height = int((height / ratio))
height -= height/11
height=int(height)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=1, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=2, column=0)
tkinter.Label(root, width=width, height=height, bg="red").grid(row=3, column=0)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=4, column=0)
tkinter.Label(root, width=width, height=height, bg='green').grid(row=5, column=0)
tkinter.Label(root, width=width, height=height, bg="red").grid(row=6, column=0)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=7, column=0)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=8, column=0)
tkinter.Label(root, width=width, height=height, bg="purple").grid(row=9, column=0)

width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

m_len = font.measure("0")
height = int(height/m_len)
width = int(width/m_len)

width = int(width / 11)
height = int((height / 11))
ratio = width/height
height = int((height / ratio))
#lower lane
just = tkinter.Label(root, width=width, height=height, bg="pink", relief=tkinter.RIDGE, highlightbackground="black",
                     highlightthickness=1).grid(row=11, column=0)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=1)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=2)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=3)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=4)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=5)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=6)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=7)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=8)
tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="pink", highlightbackground="black",
              highlightthickness=1).grid(row=11, column=9)
go_box = tkinter.Label(root, width=width, height=height, relief=tkinter.RIDGE, bg="brown", highlightbackground="black",
                       highlightthickness=1).grid(row=11, column=10)


width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight()# height of screen

m_len = font.measure("0")
height = int(height/m_len)
width = int(width/m_len)

width = int(width / 11)
height = int((height / 11))
ratio = width/height
height = int((height / ratio))
height -= height/11
height=int(height)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=1, column=10)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=2, column=10)
tkinter.Label(root, width=width, height=height, bg="red").grid(row=3, column=10)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=4, column=10)
tkinter.Label(root, width=width, height=height, bg='green').grid(row=5, column=10)
tkinter.Label(root, width=width, height=height, bg="red").grid(row=6, column=10)
tkinter.Label(root, width=width, height=height, bg="blue").grid(row=7, column=10)
tkinter.Label(root, width=width, height=height, bg="green").grid(row=8, column=10)
tkinter.Label(root, width=width, height=height, bg="purple").grid(row=9, column=10)
root.mainloop()
"""width = root.winfo_screenwidth() #width of screen
height = root.winfo_screenheight() # height of screen

m_len = font.measure("0")
height = int(height/m_len)
width = int(width/m_len)

width = int(width / 11)
height = int((height / 11))"""