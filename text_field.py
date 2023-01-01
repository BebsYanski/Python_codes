from tkinter import *
#Note that everything in tkinter is a widget.
root =Tk()

myLabel1=Label(root,text="Hello Guys",fg="dark blue",width=30).pack()

textField=Entry(root, width=30,fg="maroon", bg="#B0C4DE", borderwidth=5)
textField.pack()
textField.insert(0,"Enter Your Name")

def myClick():
	Hello="Hello "+textField.get()
	myLabel=Label(root, text= Hello)
	myLabel.pack()


#Creating a button widget
myButton1=Button(root, text="click me", state= DISABLED).pack()
myButton2=Button(root, text="CLICK ME", padx=50,pady=10,command=myClick,fg="dark blue",bg="#B0C4DE")
myButton2.pack()
#shoving it into the screen
#myButton1.pack()
#myButton2.grid(row= 1, column= 3)

root.mainloop()