from PIL import ImageTk,Image
import tkinter
root  = tkinter.Tk()

"""img = ImageTk.PhotoImage(Image.open("go_box.jpg"))
resized = img.resize((800, 600),Image.ANTIALIAS)
tkinter.Label(root,image=img).grid(row=0,column=0)"""

deathwing = Image.open('monopoly board.jpg')
image2 = deathwing.resize((1000, 700), Image.ANTIALIAS)
Deathwing2 = ImageTk.PhotoImage(image2)
tkinter.Label(root,image = Deathwing2).place(x=180,y=7)
root.mainloop()