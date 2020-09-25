import tkinter

root = tkinter.Tk()

def show():
    global widget
    widget = tkinter.Label(root,text = "hi this should get deleted")
    widget.grid()

show()
def forget_widget():
    global widget
    widget.grid_forget()

tkinter.Button(root,text="let's delete",command=lambda :forget_widget()).grid()

root.mainloop()