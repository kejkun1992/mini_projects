import time
import random
from tkinter import *

class Bomba:
    def __init__(self, płótno):
        self.płótno = płótno
        self.id = self.płótno.create_oval(0, 0, 48, 48, fill='black')
        self.płótno.move(self.id, 10, 0)
        self.y = 0
        self.płótno.bind_all('<KeyPress-Up>', self.góra)
        self.płótno.bind_all('<KeyPress-s>', self.dół)

    def rysuj(self):
        self.płótno.move(self.id, 0, self.y)
        pozycja = self.płótno.coords(self.id)
        if pozycja[1] <= 0 or pozycja[3] >= 400:
            self.y = 0

    def góra(self, zdarzenie):
        pozycja = self.płótno.coords(self.id)
        if pozycja[3] >= 400:
            self.y = -8
        
    def dół(self, zdarzenie):
        pozycja = self.płótno.coords(self.id)
        if pozycja[1] <= 0:
            self.y = 8

class Restart:
    def __init__(self, płótno):
        self.płótno = płótno
        self.płótno.bind_all('<KeyPress-Return>', self.reset)
        self.kont = False

    def reset(self, zdarzenie):
        self.kont = True

def odl_prz(przetrzymanie):
    if przetrzymanie >= 0 and przetrzymanie < 50:
        return  4
    elif przetrzymanie < 100 and przetrzymanie >=50:
        return 3
    elif przetrzymanie < 150 and przetrzymanie >=100:
        return 2
    elif przetrzymanie < 200 and przetrzymanie >=150:
        return 1
    else:
        return 0

tk = Tk()
tk.title('Gra w Bombe')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
płótno = Canvas(tk, width=400, height=400, bd=0, highlightthickness=0)
płótno.pack()
tk.update()

płótno.create_rectangle(0, 0, 400, 200, fill='blue', outline='blue')
płótno.create_rectangle(0, 201, 400, 400, fill='yellow', outline='yellow')
płótno.create_line(0, 200, 400, 200)
płótno.create_line(0, 201, 400, 201)
czas = płótno.create_text(370, 25, font=('Arial', 24),text='')
odliczanie = płótno.create_text(200, 25, font=('Arial', 24),text='')
boom = płótno.create_text(200, 200, font=('Arial', 50), text='')
odliczanie_przetrzymanie = płótno.create_text(370, 225, font=('Arial', 24),text='')
restart = Restart(płótno)
bomba = Bomba(płótno)

while 1:
 
 for i in range(1, 6):
     płótno.itemconfig(odliczanie, text=6-i)
     tk.update()
     time.sleep(1)
 płótno.itemconfig(odliczanie, text='')
 tk.update()

 x = 0

 while 1:
    
    przetrzymanie = -1
    while 1:

        x=x+1
        y = 1001-x
        
        bomba.rysuj()
        płótno.itemconfig(czas, text=y)
        tk.update_idletasks()
        tk.update()
        time.sleep(0.02)
        restart.kont = False
        przetrzymanie = przetrzymanie + 1
        pozycja = płótno.coords(bomba.id)
        płótno.itemconfig(odliczanie_przetrzymanie, text=odl_prz(przetrzymanie))
        tk.update()
        if pozycja[1] >= 160 and pozycja[3] <= 240 :
            break
        if y==0 or przetrzymanie == 200:
            break
        
    if y==0 or przetrzymanie == 200:
        break

 while 1:
     
    pozycja = płótno.coords(bomba.id)
    if pozycja[1] >= 201 or pozycja[3] <= 200:
        płótno.itemconfig(boom, text='BOOM')
    else:
        płótno.itemconfig(boom, text='REMIS')
    tk.update_idletasks()
    tk.update()

    if restart.kont == True:
        płótno.itemconfig(boom, text='')
        tk.update()
        break

    else:
        continue

 restart.kont = False
