import tkinter
import time
import random

x = random.randint(0, 600)
y = random.randint(0, 600)
def eat():
    global x
    global y
    global apple
    global rec
    x_zmei = (canvas.coords(rec)[2] + canvas.coords(rec)[0]) // 2
    y_zmei = (canvas.coords(rec)[3] + canvas.coords(rec)[1]) // 2




    if abs(x + 18 - x_zmei) < 35 and abs(y + 18 - y_zmei) < 35:
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        canvas.delete(apple)
        apple = canvas.create_rectangle(x, y, x + 35, y + 35, fill="red")



def proverka():
    global rec
    eat()
    if canvas.coords(rec)[2] > 600:
        canvas.move(rec, -600, 0)
        window.update()
    if canvas.coords(rec)[1] < 0:
        canvas.move(rec, 0, 600)
        window.update()
    if canvas.coords(rec)[3] > 600:
        canvas.move(rec, 0, -600)
        window.update()
    if canvas.coords(rec)[0] < 0:
        canvas.move(rec, 600, 0)
        window.update()



def click_down():
    while True:
        canvas.move(rec, 0, 3)
        window.update()
        time.sleep(0.01)
        proverka()


def click_up():
    while True:
        canvas.move(rec, 0, -3)
        window.update()
        time.sleep(0.01)
        proverka()

def click_left():
    while True:
        canvas.move(rec, -3, 0)
        window.update()
        time.sleep(0.01)
        proverka()

def click_right():
    while True:
        canvas.move(rec, 3, 0)
        window.update()
        time.sleep(0.01)
        proverka()



window = tkinter.Tk()
canvas = tkinter.Canvas(window, width= 600, height= 600)
window.title("Червь")
canvas.pack()
#buttons = [btn_down, btn_up]
apple = canvas.create_rectangle(x, y, x + 35, y + 35, fill="red")
rec = canvas.create_rectangle(10,  10, 45, 45, fill = "blue")

btn_down =  tkinter.Button( text="D", padx="15", pady="10", command=click_down)
btn_up=     tkinter.Button( text="U", padx="15", pady="10", command=click_up)
btn_left =  tkinter.Button( text="L", padx="15", pady="10", command=click_left)
btn_right = tkinter.Button( text="R", padx="15", pady="10", command=click_right)

btn_down.pack()
btn_up.pack()
btn_left.pack()
btn_right.pack()
btn_down.place(x=450, y=500)
btn_up.place(x=450, y=400)
btn_left.place(x=400, y=450)
btn_right.place(x=500, y=450)

window.mainloop()