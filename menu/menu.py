from tkinter import *

canvas_live = False


def destroy_canvas(event):#destroy canvas or scores
    global canvas_live
    global scores_live
    if canvas_live == True:
        canvas.quit()
        canvas.destroy()
        canvas_live = False
        menu()
    elif scores_live == True:
        label_first.quit()
        label_second.quit()
        label_third.quit()
        label_first.destroy()
        label_second.destroy()
        label_third.destroy()
        scores_download.close()
        scores_live = False
        menu()
    else:
        pass


def create_canvas(event):
    global canvas_live
    global canvas
    destroy_menu()
    canvas = Canvas(tk, width=400, height=400)
    canvas.pack()
    canvas_live = True
    tk.mainloop()


def scores_list(event):
    global scores_live, scores_download
    global label_first, label_second, label_third
    destroy_menu()
    scores_download = open('scores\\scores.txt', 'rt')
    scores_read = scores_download.read().split(',')
    label_first = Label(tk, text=scores_read[0] + ': ' + scores_read[1], font=('Arial', 30), pady=40)
    label_first.pack()
    label_second = Label(tk, text=scores_read[2] + ': ' + scores_read[3], font=('Arial', 30), pady=40)
    label_second.pack()
    label_third = Label(tk, text=scores_read[4] + ': ' + scores_read[5], font=('Arial', 30), pady=40)
    label_third.pack()
    scores_live = True
    tk.mainloop()


def destroy_tk(event):
    tk.quit()
    tk.destroy()


def menu():
    global canvas_live
    global button_start, button_exit, button_scores
    global label_1, label_2, label_3
    canvas_live = False
    button_start = Button(tk, text='START', font=('Arial', 24),background='white', relief='solid', width=10)
    button_exit = Button(tk, text='EXIT', font=('Arial', 24),background='white', relief='solid', width=10)
    button_scores = Button(tk, text='SCORES', font=('Arial', 24),background='white', relief='solid', width=10)
    label_1 = Label(tk, text='', font=('Arial', 30))
    label_2 = Label(tk, text='', font=('Arial', 30))
    label_3 = Label(tk, text='', font=('Arial', 30))
    button_start.bind('<Button-1>', create_canvas)
    button_exit.bind('<Button-1>', destroy_tk)
    button_scores.bind('<Button-1>', scores_list)
    label_1.pack()
    button_start.pack()
    label_2.pack()
    button_scores.pack()
    label_3.pack()
    button_exit.pack()
    tk.mainloop()


def destroy_menu():
    button_start.quit()
    button_exit.quit()
    button_scores.quit()
    button_start.destroy()
    button_exit.destroy()
    button_scores.destroy()
    label_1.quit()
    label_2.quit()
    label_3.quit()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()

tk =Tk()
tk.resizable(0,0)
tk.title('Menu')
tk.wm_attributes('-topmost',1)
tk.geometry('400x400')
tk.bind_all('<Escape>', destroy_canvas)

menu()




