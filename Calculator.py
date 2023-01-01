from tkinter import *
root = Tk()
root.title("My Calculator")
root.iconbitmap('C:\\Users\\dell\\Documents\\Python_codes\\icons\\4.ico')


#head=Label(root,text="My Calculator").grid()

screen = Entry(root,width=50,borderwidth=5)
screen.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

def but_clr():
	screen.delete(0, END)

def but_add():
	global sign
	sign= "+"
	first_number=screen.get()
	print(first_number)
	global first_n 
	first_n= int(first_number)
	screen.delete(0, END)

def but_sub():
	global sign
	sign= "-"
	first_number=screen.get()
	global first_n 
	first_n= int(first_number)
	screen.delete(0, END)
	

def but_mul():
	global sign
	sign= "*"
	first_number=screen.get()
	global first_n 
	first_n= int(first_number)
	screen.delete(0, END)

def but_div():
	global sign
	sign= "/"
	first_number=screen.get()
	global first_n 
	first_n= int(first_number)
	screen.delete(0, END)
	pass

def but_mod():
	global sign
	sign= "%"
	first_number=screen.get()
	global first_n 
	first_n= int(first_number)
	screen.delete(0, END)
	pass

def but_eq():
	current=screen.get()
	screen.delete(0, END)

	if sign=="+":
		screen.insert(0,first_n + int(current))

	elif sign=="-":
		screen.insert(0,first_n - int(current))

	elif sign=="*" :
		screen.insert(0,first_n * int(current))

	elif sign=="/" :
		screen.insert(0,first_n / int(current))


	elif sign=="%" :
		screen.insert(0,first_n % int(current))

	else:
		screen.insert(0,"ERROR")


def but_click(number):
	#screen.delete(0, END)
	current=screen.get()
	screen.delete(0, END)
	screen.insert(0, str(current)+str(number))
	#return

#Here, we  define our buttons (Lambda is used to enable the use of arguments)
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
but_sub=Button(root,text='-',padx=40,pady=20,command=but_sub)
but_mul=Button(root,text='*',padx=40,pady=20,command=but_mul)
but_div=Button(root,text='/',padx=40,pady=20,command=but_div)
but_mod=Button(root,text='%',padx=40,pady=20,command=but_mod)

but_equal=Button(root,text='=',padx=140,pady=20,command=but_eq)
but_clr=Button(root,text='clear',padx=80,pady=20,command=but_clr)

#Here, we arrange the buttons on the screen
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

but_add.grid(row=1,column=5)
but_sub.grid(row=2,column=5)
but_mul.grid(row=3,column=5)
but_div.grid(row=4,column=5)
but_mod.grid(row=5,column=5)

but_equal.grid(row=5,column=0,columnspan=3)
but_clr.grid(row=4,column=1,columnspan=2)

root.mainloop()