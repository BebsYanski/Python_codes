from tkinter import *

root= Tk()
root.title("YANSKI")
root.iconbitmap("C:\icon\Chemonics-International.ico")  #Here, we have used an icon for our root.




def but_click(number):
	global current
	current=screen.get()
	screen.delete(0,END)
	screen.insert(0,str(current) + str(number))
	pass


def but_add():
	first_num=screen.get()
	global first_n
	first_n=int(first_num)
	screen.delete(0,END)
	pass


def but_equal():
	
	current=screen.get()
	screen.delete(0,END)
	screen.insert(0,first_n + int(current) )
	pass



def but_clear():
	screen.delete(0,END)
	pass


screen= Entry(root, width=35,borderwidth=5)
screen.grid(padx=10,pady=10,columnspan=3)



exit_but= Button(root,text="EXIT PROGRAM",pady=20,command=root.quit)  #Here, we added an exit button
exit_but.grid(row=5,column=2)


but1=Button(root,text=1,padx=40,pady=20,command=lambda: but_click(1))
but2=Button(root,text=2,padx=40,pady=20,command=lambda: but_click(2))
but3=Button(root,text=3,padx=40,pady=20,command=lambda: but_click(3))
but4=Button(root,text=4,padx=40,pady=20,command=lambda: but_click(4))
but5=Button(root,text=5,padx=40,pady=20,command=lambda: but_click(5))
but6=Button(root,text=6,padx=40,pady=20,command=lambda: but_click(6))
but7=Button(root,text=7,padx=40,pady=20,command=lambda: but_click(7))
but8=Button(root,text=8,padx=40,pady=20,command=lambda: but_click(8))
but9=Button(root,text=9,padx=40,pady=20,command=lambda: but_click(9))
but0=Button(root,text=0,padx=40,pady=20,command=lambda: but_click(0))

but_add=Button(root,text='+',padx=40,pady=20,command=but_add)
but_clear=Button(root,text='clear',padx=30,pady=20,command=but_clear)
but_equal=Button(root,text='=',padx=88,pady=20,command=but_equal)


but1.grid(row=3,column=0)
but2.grid(row=3,column=1)
but3.grid(row=3,column=2)
but4.grid(row=2,column=0)
but5.grid(row=2,column=1)
but6.grid(row=2,column=2)
but7.grid(row=1,column=0)
but8.grid(row=1,column=1)
but9.grid(row=1,column=2)
but0.grid(row=4,column=0)

but_add.grid(row=4,column=1)
but_clear.grid(row=4,column=2)
but_equal.grid(row=5,column=0,columnspan=2)



root.mainloop()