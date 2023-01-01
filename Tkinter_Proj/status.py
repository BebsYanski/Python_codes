from tkinter import *
from PIL import ImageTk,Image

root = Tk();
root.title("Images and Icons with Python")
root.iconbitmap('C:\\Users\\dell\\Documents\\Python_codes\\icons\\3.ico')

my_img1 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\1.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\2.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\3.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\4.jpg"))
my_img5 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\5.jpg"))
my_img6 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\6.jpg"))
my_img7 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\7.jpg"))
my_img8 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\8.jpg"))
my_img9 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\9.jpg"))
my_img10 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\10.jpg"))
my_img11 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\11.jpg"))
my_img12 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\12.jpg"))
my_img13 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\13.jpg"))
my_img14 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\14.jpg"))
my_img15 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\15.jpg"))
my_img16 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\16.jpg"))
my_img17 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\17.jpg"))
my_img18 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\18.jpg"))
my_img19 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\19.jpg"))
my_img20 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\20.jpg"))
my_img21 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\21.jpg"))
my_img22 = ImageTk.PhotoImage(Image.open("C:\\Users\\dell\\Documents\\Python_codes\\images\\22.jpg"))

image_list = [my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7,my_img8,my_img9,my_img10,my_img11
,my_img12,my_img13,my_img14,my_img15,my_img16,my_img17,my_img18,my_img19,my_img20,my_img21,my_img22]


#Status code

status = Label(root, text= "Image 1 of "+str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)


my_label = Label(image=image_list[0])
my_label.grid(row=0,column=0,columnspan=3)

def forward(image_number):
  global my_label
  global button_forward
  global button_back

  
  my_label.grid_forget()
  
  my_label = Label(image=image_list[image_number - 1])

  

  button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
  button_back = Button(root, text="<<" , command=lambda: back(image_number-1))

  if image_number == 22:
    button_forward = Button(root, text=">>", state=DISABLED)

  my_label.grid(row=0,column=0,columnspan=3)
  button_forward.grid(row=1,column=2)
  button_back.grid(row=1,column=0)

  status = Label(root, text= "Image "+str(image_number)+" of "+str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)
  status.grid(row=3,column=0,columnspan= 3, sticky=W+E)



def back(image_number):
  global my_label
  global button_forward
  global button_back
  
  my_label.grid_forget()
  my_label = Label(image=image_list[image_number - 1])

  button_forward = Button(root, text=">>", command=lambda:forward(image_number+1))
  button_back = Button(root, text="<<" , command=lambda: back(image_number-1))

  if image_number == 1:
    button_back = Button(root, text="<<", state=DISABLED)


  my_label.grid(row=0,column=0,columnspan=3)
  button_forward.grid(row=1,column=2)
  button_back.grid(row=1,column=0)

  status = Label(root, text= "Image "+ str(image_number)+" of "+str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)
  status.grid(row=3,column=0,columnspan= 3, sticky=W+E)



button_back = Button(root, text="<<" , command=back, state=DISABLED)
# button_back = Button(root, text="<<", state=DISABLED)

button_exit = Button(root, text="Exit Program", command = root.quit)
button_forward = Button(root, text=">>", command=lambda:forward(2))


button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2, pady=10)
status.grid(row=3,column=0,columnspan= 3, sticky=W+E)








def search():
  global Find
  global my_label
  global button_forward
  global button_back

  find = search_field.get()
  print(find)
  my_label.grid_forget()
  my_label = Label(image=image_list[int(find)])
  my_label.grid(row=0,column=0,columnspan=3)
  status = Label(root, text= "Image "+ str(find)+" of "+str(len(image_list)),bd=1, relief=SUNKEN, anchor=E)
  status.grid(row=3,column=0,columnspan= 3, sticky=W+E)

  
  

search_field = Entry(root, width=20, borderwidth=5, font="arial")
but_search = Button(root, text="Search",fg="blue",bg="#992",command=search)

but_search.grid(row=2,column=2)
search_field.grid(row=2,column=0,columnspan=3,pady=20)

root.mainloop()