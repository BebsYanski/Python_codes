from tkinter import *

root =Tk()
#Creating a label widget
myLabel1=Label(root, text="Hello World?")
myLabel2=Label(root, text="Hello dr, how are you?")
#shoving it into the screen
myLabel1.grid(row= 0, column= 8)
myLabel2.grid(row= 1, column= 3)

root.mainloop()