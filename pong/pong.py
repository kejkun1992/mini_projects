import random
import time
from tkinter import*

'''declaration of class Ball and Rocket'''

class Ball:
    def __init__(self, canvas, colour, right_rocket, left_rocket, right_score, left_score):
        self.canvas = canvas
        self.right_rocket = right_rocket
        self.left_rocket = left_rocket
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=colour, outline='black')
        self.canvas.move(self.id, 590, 140)
        self.positive_list = [8, 9, 10]
        self.negative_list = [-8, -9, -10]
        self.positive_list_1 = 1*[3, 2, 1]
        self.negative_list_1 = 1*[-3, -2, -1]
        self.x = random.choice([-6, 6])
        self.y = random.choice([-6, 6])
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.right_score = right_score
        self.left_score = left_score
        self.left_side = False
        self.right_side = False
        
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            time.sleep(0.1)
            self.canvas.move(self.id, 130, 0)
            self.right_score = self.right_score + 1
            self.left_side = True
            self.x = random.choice(self.positive_list)
            self.y = random.choice(self.positive_list_1)
        if position[2] >= self.canvas_width:
            time.sleep(0.1)
            self.canvas.move(self.id, -130, 0)
            self.left_score = self.left_score + 1
            self.right_side = True
            self.x = random.choice(self.negative_list)
            self.y = random.choice(self.negative_list_1)
        if position[1] <= 0:
            self.y = random.choice(self.positive_list_1)
        if position[3] >= self.canvas_height:
            self.y = random.choice(self.negative_list_1)
        if self.left_hit(position) == True:
            self.x = random.choice(self.positive_list)
        if self.right_hit(position) == True:
            self.x = random.choice(self.negative_list)

    def left_hit(self,position):
        left_rocket_position = self.canvas.coords(self.left_rocket.id)
        if position[3] >= left_rocket_position[1] and position[1] <= left_rocket_position[3]:
            if position[0] <= left_rocket_position[2] and position[0] > left_rocket_position[0]:
                return True
        return False

    def right_hit(self,position):
        right_rocket_position = self.canvas.coords(self.right_rocket.id)
        if position[3] >= right_rocket_position[1] and position[1] <= right_rocket_position[3]:
            if position[2] >= right_rocket_position[0] and position[2] < right_rocket_position[2]:
                return True
        return False

class Rocket:
    def __init__(self, canvas, colour, side):
        self.canvas = canvas
        self.side = side
        self.id=self.canvas.create_rectangle(10, 10, 30, 100, fill=colour, outline=colour)
        self.x = 0
        self.y = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        if self.side == 0:
            self.canvas.move(self.id, 70, 0)
            self.canvas.bind_all('<KeyPress-w>', self.left_up)
            self.canvas.bind_all('<KeyPress-s>', self.left_down)
        if self.side == 1:
            self.canvas.move(self.id, 1100, 0)
            self.canvas.bind_all('<KeyPress-Up>', self.right_up)
            self.canvas.bind_all('<KeyPress-Down>', self.right_down)

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 0
        if position[3] >= self.canvas_height:
            self.y = 0
       
    def left_up(self, event):
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 0
        else:
            self.y = -8

    def left_down(self, event):
        position = self.canvas.coords(self.id)
        if position[3] >= self.canvas_height:
            self.y = 0
        else:
            self.y = 8

    def right_up(self, event):
        position = self.canvas.coords(self.id)
        if position[1] <= 0:
            self.y = 0
        else:
            self.y = -8

    def right_down(self, event):
        position = self.canvas.coords(self.id)
        if position[3] >= self.canvas_height:
            self.y = 0
        else:
            self.y = 8

'''declaration of menu's function and game's mainloop'''

canvas_live = False # canvas can be destroyed or not
break_live = False  # if True break loop

def destroy_canvas(event):
    global canvas_live
    if canvas_live == True:
        canvas.quit()
        canvas.destroy()
        canvas_live = False
        menu()
    else:
        pass

def menu():
    global canvas_live
    global button_start, button_exit
    global label_1, label_2
    global break_live
    break_live = True
    canvas_live = False
    button_start = Button(tk, text='START', font=('Arial', 24),background='white', relief='solid', width=10)
    button_exit = Button(tk, text='EXIT', font=('Arial', 24),background='white', relief='solid', width=10)
    label_1 = Label(tk, text='', font=('Arial',32))
    label_2 = Label(tk, text='', font=('Arial',32))
    button_start.bind('<Button-1>', game)
    button_exit.bind('<Button-1>', destroy_tk)
    label_1.pack()
    button_start.pack()
    label_2.pack()
    button_exit.pack()
    tk.mainloop()

def destroy_tk(event):
    tk.quit()
    tk.destroy()

def game(event):
    global canvas_live
    global canvas
    global break_live
    break_live = False
    button_start.quit()
    button_exit.quit()
    button_start.destroy()
    button_exit.destroy()
    label_1.quit()
    label_2.quit()
    label_1.destroy()
    label_2.destroy()
    canvas = Canvas(tk, width=1200, height=300, bd=0, highlightthickness=0)
    canvas.pack()
    canvas_live = True
    tk.update()

    right_rocket = Rocket(canvas, 'blue', 1)
    left_rocket = Rocket(canvas, 'black', 0)
    ball = Ball(canvas, 'red', right_rocket, left_rocket, 0, 0)

    text1 = canvas.create_text(600, 30, text='', font=('Arial', 24))
    text2 = canvas.create_text(30, 30, text=ball.left_score, font=('Arial', 24))
    text3 = canvas.create_text(1170, 30, text=ball.right_score, font=('Arial', 24))

    while 1:
        
        ball.right_score = 0
        ball.left_score = 0
        canvas.itemconfig(text2, text=ball.left_score)
        canvas.itemconfig(text3, text=ball.right_score)
        tk.update()
        for x in range(0,5):
            canvas_live = False
            canvas.itemconfig(text1, text=str(5-x))
            tk.update()
            time.sleep(1)
        canvas_live = True
        canvas.itemconfig(text1, text='')

        while 1:

            ball.draw()
            left_rocket.draw()
            right_rocket.draw()
            if  ball.left_side == True or ball.right_side == True:
                canvas_live = False
                canvas.itemconfig(text1, text='POINT')
                tk.update()
                time.sleep(2)
                canvas.itemconfig(text1, text='')
                canvas.itemconfig(text2, text=ball.left_score)
                canvas.itemconfig(text3, text=ball.right_score)
                ball.left_side = False
                ball.right_side = False
                canvas_live = True
            tk.update()
            time.sleep(0.01)
            menu_appear = 0 # when next loop end
            
            while ball.right_score == 5:
                canvas_live = False
                menu_appear = menu_appear + 1
                canvas.itemconfig(text1, text='BLUE WIN', font=('Arial', 24))
                tk.update()
                time.sleep(0.5)
                canvas.itemconfig(text1, text='')
                tk.update()
                time.sleep(0.5)
                if menu_appear == 4:
                    break_live = True
                    canvas.itemconfig(text1, text='BLUE WIN', font=('Arial', 24))
                    break
                
            while ball.left_score == 5:
                canvas_live = False
                menu_appear = menu_appear + 1
                canvas.itemconfig(text1, text='BLACK WIN', font=('Arial', 24))
                tk.update()
                time.sleep(0.5)
                canvas.itemconfig(text1, text='')
                tk.update()
                time.sleep(0.5)
                if menu_appear == 4:
                    break_live = True
                    canvas.itemconfig(text1, text='BLACK WIN', font=('Arial', 24))
                    break

            if break_live == True:
                    break

        if break_live == True:
            canvas_live = True
            break

    tk.mainloop()
                
tk =Tk()
tk.resizable(0,0)
tk.title('Pong')
tk.wm_attributes('-topmost',1)
tk.geometry('1200x300')
tk.bind_all('<Escape>', destroy_canvas)

menu()
