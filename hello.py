from tkinter import *
#Note that everything in tkinter is a widget.
root =Tk()

myLabel=Label(root, text="Hello dr, how are you?")
newLabel=Label(root, text="Hello dr, I'm Good")

myLabel.pack()
newLabel.pack()

root.mainloop()