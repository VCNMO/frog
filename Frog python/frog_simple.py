from tkinter import *

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
    lbl_step = Label(text="Количество шагов - 0")
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
    # проверка на соседство лягушек и пустого поля
    if 0 < abs(btn.winfo_x() - empty_button.winfo_x()) <= 210:
        
        # если все по правилам, то меняем кнопки местами
        #swap_frog(btn.winfo_x(), empty_button.winfo_x())
        
        # преобразовали к типу картинки
        #img = btn.cget('image')
        #empty_button.configure(image=img)
        #btn.configure(image=frog_empty)
        #empty_button = btn
        temp_x = btn.winfo_x()
        btn.place(x=empty_button.winfo_x(), y=0)
        empty_button.place(x=temp_x, y=0)
        
        
        #if is_game_end():
            #if step == 24:
                #lbl_step.configure(text="ПОБЕДА!")
            #else:
                #lbl_step.configure(text="Надо выполнить за 24 шага, а не за " + str(step))
        #else:
            #step += 1
            #lbl_step.configure(text="Количество шагов - " + str(step))
        

win = Tk()
win.geometry("944x250")
win.title("Лягушка-попрыгушка")

frog_left = PhotoImage(file="frog1.png")
frog_empty = PhotoImage(file="list.png")
frog_right = PhotoImage(file="frog2.png")

# создание всех кнопок с лягушками
for i in range(4):
    btn1 = Button(image=frog_left)
    btn1.place(x=105 * i, y=0)
    btn1.bind('<Button-1>', click_frog)
    list_btn.append(btn1)
    
# создание пустого листа
empty_button = Button(image=frog_empty)
empty_button.place(x=4*105, y=0)
empty_button.bind('<Button-1>', click_frog)
#list_btn.append(btn2)

# создание кнопок с лягушками влевл   
for i in range(4):    
    btn1 = Button(image=frog_right)
    btn1.place(x=105 * (i + 5), y=0)    
    btn1.bind('<Button-1>', click_frog)
    #list_btn.append(btn1)

# создание поля для вывода числа шагов
lbl_step = Label(text="Количество шагов - 0")
lbl_step.place(x=10, y=150)

# кнопка начало игры
btn_new_game = Button(text="Новая игра", command=new_game)
btn_new_game.place(x=300, y=150)

#new_game()

win.mainloop()

