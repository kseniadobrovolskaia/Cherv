import tkinter
import time
import random

x = random.randint(0, 600)
y = random.randint(0, 600)
def eat():
    global x, y, x0, y0, app, apple

    if abs(x - x0) < 35 and abs(y - y0) < 35:
        app += 1
        x = random.randint(0, 600)
        y = random.randint(0, 600)
        canvas.delete(apple)
        apple = canvas.create_rectangle(x, y, x + 35, y + 35, fill="red")


def proverka():
    global rec, x0, y0
    eat()

    if (y0 + 36) > 600:
        y0 -= 600
    if x0 < 0:
        x0 += 600
    if (x0 + 36) > 600:
        x0 -= 600
    if y0 < 0:
        y0 += 600
    canvas.delete(rec)
    rec = canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline="blue")
    window.update()




def click_down():
    global rec, x0, y0, count, app
    while True:
        if count < 12 * app:
            cherv.append(canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline="blue"))
            count += 1

        for i in range(len(cherv)):
            canvas.delete(cherv[i])
            cherv[i] = canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline="blue")
            proverka()
            window.update()
            time.sleep(0.01)
            y0 += 3


def click_up():
   global rec, x0, y0, count, app
   while True:
       if count < 12 * app:
            cherv.append(canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline="blue"))
            count += 1
       for i in range(len(cherv)):
           canvas.delete(cherv[i])
           cherv[i] = canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline="blue")
           proverka()
           window.update()
           time.sleep(0.01)
           y0 -= 3



def click_left():
    global rec, x0, y0, count, app
    while True:
        if count < 12 * app:
            cherv.append(canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline = "blue"))
            count += 1
        for i in range(len(cherv)):
            canvas.delete(cherv[i])
            cherv[i] = canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline = "blue")
            proverka()
            window.update()
            time.sleep(0.01)
            x0 -= 3



def click_right():
    global rec, x0, y0, count, app
    while True:
        if count < 12 * app:
            cherv.append(canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline = "blue"))
            count += 1
        for i in range(len(cherv)):
            canvas.delete(cherv[i])
            cherv[i] = canvas.create_rectangle(x0, y0, x0 + 36, y0 + 36, fill="blue", outline = "blue")
            proverka()
            window.update()
            time.sleep(0.01)
            x0 += 3



window = tkinter.Tk()
canvas = tkinter.Canvas(window, width= 600, height= 600)
window.title("Червь")
canvas.pack()

apple = canvas.create_rectangle(x, y, x + 35, y + 35, fill = "red")
x0 = 10
y0 = 10

rec = canvas.create_rectangle(10,  10, 45, 45, fill = "blue", outline= "blue")
cherv = []
cherv.append(rec)
count = 0
app = 0



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
