import turtle, random
from tkinter import*

color_list = [0, 0.10, 0.20, 0.30, 0.40, 0.5, 0.60, 0.70, 0.80, 0.90, 1]


def close_window(event):
    window.quit()
    window.destroy()


def menu():
    global turtle, window, entry
    window = Tk()
    window.resizable(0, 0)
    window.title('Polygons')
    window.wm_attributes('-topmost', 1)
    entry = Entry(window, relief='solid', width=15, font=('Arial', 20))
    entry.pack()
    start_button = Button(window, text='POLYGON', font=('Arial', 20, 'bold'),
                            foreground='blue', background='white', relief='solid', width=10, activebackground='white',activeforeground='blue' )
    button_exit = Button(window ,text = 'EXIT' ,font=('Arial',20,'bold'),
                           foreground='red', background='white', relief='solid', width=10, activebackground='white',activeforeground='red')
    button_star = Button(window, text='STAR', font=('Arial', 20, 'bold'),
                               foreground='yellow', background='white', relief='solid', width=10, activebackground='white', activeforeground='yellow')
    start_button.pack()
    start_button.bind('<Button-1>', draw)
    button_exit.bind_all('<Escape>', close_window)
    button_star.pack()
    button_exit.bind('<Button-1>', close_window)
    button_exit.pack()
    button_star.bind('<Button-1>', draw_star)
    canvas = Canvas(window, width=400, height=400)
    canvas.pack()
    turtle=turtle.RawPen(canvas)
    window.mainloop()

    
def draw_star(event):
    try:
        number_of_angles = entry.get()
        n = int(number_of_angles)
        turtle.reset()
        
        R = random.choice(color_list)
        G = random.choice(color_list)
        B = random.choice(color_list)
        if n % 2 == 1 and n not in [1, 2, 3]:
            turtle.color(R, G, B)
            turtle.left(180 - 2 * (180 - (n-20/n * 180)))
            for x in range(0, n):
                turtle.forward(800/n)
                turtle.left(180 - (180 - 2 * (180 -(n - 2)/n * 180)))
        if n % 2 == 0 or n in [1, 2, 3]:
            pass
    except:
        pass
               

def draw(event):
    try:
        number_of_sides = entry.get()
        n = int(number_of_sides)
        angle = 180 - ((n - 2) / n * 180)
        turtle.reset()

        R = random.choice(color_list)
        G = random.choice(color_list)
        B = random.choice(color_list)
        
        if n not in [1, 2]:
            turtle.color(R, G, B)
            for x in range(0, n):
                turtle.forward(300/n)
                turtle.left(angle)
        else:
            pass
    except:
        pass

menu()   
            
                           
