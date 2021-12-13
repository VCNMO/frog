from tkinter import *
from PIL import Image, ImageTk

empty_button = ""
def click_frog(event):
    global empty_button
    btn = event.widget
    if abs(btn.winfo_x() - empty_button.winfo_x()) <= 208:
        img = btn.cget('image')
        empty_button.configure(image=img)
        btn.configure(image=frog_empty)
        empty_button = btn

win = Tk()
win.geometry("944x150")
win.title("Ћ€гушка-попрыгушка")

frog_left = ImageTk.PhotoImage(Image.open("frog1.png"))
frog_empty = ImageTk.PhotoImage(Image.open("list.png"))
frog_right = ImageTk.PhotoImage(Image.open("frog2.png"))

for i in range(4):
    btn1 = Button(image=frog_left)
    btn1.place(x=104 * i, y=0)
    btn1.bind('<Button-1>', click_frog)

btn2 = Button(image=frog_empty)
btn2.place(x=4*104, y=0)
btn2.bind('<Button-1>', click_frog)

empty_button = btn2
    
for i in range(4):    
    btn1 = Button(image=frog_right)
    btn1.place(x=104 * (i + 5), y=0)    
    btn1.bind('<Button-1>', click_frog)


win.mainloop()

