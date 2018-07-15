from time import sleep
import random
from tkinter import *


class Bomb:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = self.canvas.create_oval(0, 0, 48, 48, fill='black')
        self.canvas.move(self.id, 10, 0)
        self.y = 0
        self.canvas.bind_all('<KeyPress-Up>', self.up)
        self.canvas.bind_all('<KeyPress-s>', self.down)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0 or position[3] >= 400:
            self.y = 0

    def up(self, event):
        position = self.canvas.coords(self.id)
        if position[3] >= 400:
            self.y = -8
        
    def down(self, event):
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 8


class Restart:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<KeyPress-Return>', self.reset)
        self.cont = False

    def reset(self, event):
        self.cont = True


def count_hold(hold):
    if hold >= 0 and hold < 50:
        return  4
    elif hold < 100 and hold >=50:
        return 3
    elif hold < 150 and hold >=100:
        return 2
    elif hold < 200 and hold >=150:
        return 1
    else:
        return 0

tk = Tk()
tk.title('Gra w Bombe')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

canvas.create_rectangle(0, 0, 400, 200, fill='blue', outline='blue')
canvas.create_rectangle(0, 201, 400, 400, fill='yellow', outline='yellow')
canvas.create_line(0, 200, 400, 200)
canvas.create_line(0, 201, 400, 201)
time = canvas.create_text(370, 25, font=('Arial', 24),text='')
counting = canvas.create_text(200, 25, font=('Arial', 24),text='')
boom = canvas.create_text(200, 200, font=('Arial', 50), text='')
counting_hold = canvas.create_text(370, 225, font=('Arial', 24),text='')
restart = Restart(canvas)
bomb = Bomb(canvas)

while 1:
 
 for i in range(1, 6):
     canvas.itemconfig(counting, text=6-i)
     tk.update()
     sleep(1)
 canvas.itemconfig(counting, text='')
 tk.update()

 x = 0

 while 1:
    
    hold = -1
    while 1:

        x=x+1
        y = 1001-x
        
        bomb.draw()
        canvas.itemconfig(time, text=y)
        tk.update_idletasks()
        tk.update()
        sleep(0.02)
        restart.cont = False
        hold = hold + 1
        position = canvas.coords(bomb.id)
        canvas.itemconfig(counting_hold, text=count_hold(hold))
        tk.update()
        if position[1] >= 160 and position[3] <= 240 :
            break
        if y==0 or hold == 200:
            break
        
    if y==0 or hold == 200:
        break

 while 1:
     
    position = canvas.coords(bomb.id)
    if position[1] >= 201 or position[3] <= 200:
        canvas.itemconfig(boom, text='BOOM')
    else:
        canvas.itemconfig(boom, text='DRAW')
    tk.update_idletasks()
    tk.update()

    if restart.cont == True:
        canvas.itemconfig(boom, text='')
        tk.update()
        break

    else:
        continue

 restart.cont = False
