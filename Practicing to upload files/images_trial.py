import tkinter
from PIL import ImageTk,Image
window = tkinter.Tk()
load = Image.open("go_box.jpg")
render = ImageTk.PhotoImage(load)

img =tkinter.Label(window,image = render)
img.place(x=0, y=0)
window.mainloop()