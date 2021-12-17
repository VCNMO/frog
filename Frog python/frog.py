from tkinter import *
from PIL import Image, ImageTk

list_btn = list()

def new_game():
    global step, frog, empty_button
    step = 0
    frog = [1, 1, 1, 1, 0, 2, 2, 2, 2]    
    for i, btn in enumerate(list_btn):
        if i < 4:
            btn.configure(image=frog_left)
        elif i > 4:
            btn.configure(image=frog_right)
        else:
            btn.configure(image=frog_empty)
    lbl_step = Label(text="���������� ����� - 0")
    empty_button = list_btn[4]
            
            
def swap_frog(x_frog1, x_frog2):
    ind_frog1 = x_frog1 // 104
    ind_frog2 = x_frog2 // 104
    frog[ind_frog1], frog[ind_frog2] = frog[ind_frog2], frog[ind_frog1]
    print(frog)

def is_game_end():
    k = 0
    for i in range(4):
        if frog[i] == 2:
            k += 1
    if k == 4 and frog[4] == 0:
        return True
    return False

def click_frog(event):
    global empty_button, step
    btn = event.widget
    if 0 < abs(btn.winfo_x() - empty_button.winfo_x()) <= 208:
        
        swap_frog(btn.winfo_x(), empty_button.winfo_x())
        
        img = btn.cget('image')
        empty_button.configure(image=img)
        btn.configure(image=frog_empty)
        empty_button = btn
        
        
        if is_game_end():
            if step == 24:
                lbl_step.configure(text="������!")
            else:
                lbl_step.configure(text="���� ��������� �� 24 ����, � �� �� " + str(step))
        else:
            step += 1
            lbl_step.configure(text="���������� ����� - " + str(step))
        

win = Tk()
win.geometry("944x250")
win.title("�������-����������")

frog_left = ImageTk.PhotoImage(Image.open("frog1.png"))
frog_empty = ImageTk.PhotoImage(Image.open("list.png"))
frog_right = ImageTk.PhotoImage(Image.open("frog2.png"))

# �������� ���� ������ � ���������
for i in range(4):
    btn1 = Button(image=frog_left)
    btn1.place(x=104 * i, y=0)
    btn1.bind('<Button-1>', click_frog)
    list_btn.append(btn1)

btn2 = Button(image=frog_empty)
btn2.place(x=4*104, y=0)
btn2.bind('<Button-1>', click_frog)
list_btn.append(btn2)
empty_button = btn2
    
for i in range(4):    
    btn1 = Button(image=frog_right)
    btn1.place(x=104 * (i + 5), y=0)    
    btn1.bind('<Button-1>', click_frog)
    list_btn.append(btn1)

# �������� ���� ��� ������ ����� �����
lbl_step = Label(text="���������� ����� - 0")
lbl_step.place(x=10, y=150)

# ������ ������ ����
btn_new_game = Button(text="����� ����", command=new_game)
btn_new_game.place(x=300, y=150)

new_game()

win.mainloop()

