import tkinter
from PIL import Image, ImageTk
from PIL import resize
from PIL import ImageTk,Image
window = tkinter.Tk()
load = Image.open("go_box.jpg")
render = ImageTk.PhotoImage(load)

img =tkinter.Label(window,image = render)
img = img.resize((250, 250), Image.ANTIALIAS)
img.place(x=0, y=0)
window.mainloop()