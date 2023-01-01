from tkinter import *
#Note that everything in tkinter is a widget.
root =Tk()

def myClick():
	myLabel=Label(root, text= "You clicked a button")
	myLabel.grid()
#Creating a button widget
myButton1=Button(root, text="click me", state= DISABLED).grid()
myButton2=Button(root, text="Next", padx=50,pady=10,command=myClick,fg="dark blue",bg="#B0C4DE")
myButton2.grid(row= 1, column= 3)
#shoving it into the screen
#myButton1.pack()
#myButton2.grid(row= 1, column= 3)

root.mainloop()