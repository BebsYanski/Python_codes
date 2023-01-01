from tkinter import *

root=Tk()

label=Label(root,text="What is Your name?",fg="indigo")
label.grid();

TextField=Entry(root,borderwidth=5)
TextField.grid(padx=10,pady=10,columnspan=2)

okBut=Button(root,text="OK",padx=20,pady=10)
okBut.grid(row=2,column=0)

cancelBut=Button(root,text="Cancel",padx=30,pady=10,fg="blue")
cancelBut.grid(row=2,column=1)


root.mainloop()