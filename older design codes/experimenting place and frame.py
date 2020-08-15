"""import tkinter
root = tkinter.Tk()
frame1 = tkinter.Frame(root,bg="blue",width=40,height=40)
frame2 = tkinter.Frame(root,bg="red",width=40,height=40)
frame2.pack(side="bottom")
frame1.pack(side="top")
token1 = tkinter.Label(frame1,bg = "green" , width = 2,height = 2)
token2 = tkinter.Label(frame2,bg = "orange" , width = 2,height = 2)
token1.pack(side = "left")
token2.pack(side= "right")

root.mainloop()"""

import cv2
img = cv2.imread("monopoly board.jpg" , 1)
cv2.imshow("window" , img)
cv2.waitKey(0)
cv2.destroyWindow("window")