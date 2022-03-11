
import tkinter
import time
import random

razmer_okna = 600
razmer_apple = 36
step = 3
speed = 0.01


x = random.randint(0, razmer_okna) #magic number!
y = random.randint(0, razmer_okna)

def eat():
    global x, y, x0, y0, app, apple, siel

    if abs(x - x0) < razmer_apple and abs(y - y0) < razmer_apple: #magic number
        app += 1
        x = random.randint(0, razmer_okna)
        y = random.randint(0, razmer_okna)
        canvas.delete(apple)
        apple = canvas.create_rectangle(x, y, x + razmer_apple, y + razmer_apple, fill="red")
        siel = 24



def proverka(i):
    global rec, x0, y0, siel
    eat()

    if (y0 + razmer_apple) > razmer_okna:
        y0 -= razmer_okna
    if x0 < 0:
        x0 += razmer_okna
    if (x0 + razmer_apple) > razmer_okna:
        x0 -= razmer_okna
    if y0 < 0:
        y0 += razmer_okna
    if len(cherv) > 50 and siel < 0:
        num = i - 24

        # while num != (i + 1):
        #     if num < 0:
        #         num += len(cherv)
        #
        #     if i == len(cherv) and num == 0:
        #         break
        #
        #     if (abs(canvas.coords(cherv[num])[0] - canvas.coords(cherv[i])[0]) < razmer_apple) and (abs(canvas.coords(cherv[num])[1] - canvas.coords(cherv[i])[1]) < razmer_apple):
        #         print(i)
        #         print(num)
        #         print(x0)
        #         print(y0)
        #         print(canvas.coords(cherv[i])[0])
        #         print(canvas.coords(cherv[i])[1])
        #         print(canvas.coords(cherv[num])[0])
        #         print(canvas.coords(cherv[num])[1])
        #
        #         print(len(cherv))
        #         window.mainloop()
        #     num -= 1
        canvas.delete(rec)
        rec = canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue", outline="blue")
        window.update()

def move():
    global rec, x0, y0, count, app, step, start, siel, side
    start = 1
    while True:
        if count < app:
            for i in range(razmer_apple // step):
                cherv.append(canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue", outline="blue"))
            count += 1

        for i in range(len(cherv)):
            siel -= 1
            canvas.delete(cherv[i])
            cherv[i] = canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue", outline="blue")
            proverka(i)
            window.update()
            time.sleep(speed)
            if side == 'up':
                y0 -= step
            elif side == 'right':
                x0 += step
            elif side == 'down':
                y0 += step
            else:
                x0 -= step


def click_down(event):
    global side, start
    side = 'down'
    if start == 0:
        move()


def click_up(event):
   global side, start
   side = 'up'
   if start == 0:
       move()



def click_left(event):
    global side, start
    side = 'left'
    if start == 0:
        move()



def click_right(event):
    global side, start
    side = 'right'
    if start == 0:
        move()


if __name__ == '__main__':
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width= razmer_okna, height= razmer_okna)
    window.title("Червь")
    canvas.pack()

    apple = canvas.create_rectangle(x, y, x + razmer_apple, y + razmer_apple, fill = "red")
    x0 = 10
    y0 = 10
    start = 0

    rec = canvas.create_rectangle(x0,  y0, x0 + razmer_apple, y0 + razmer_apple, fill = "blue", outline= "blue")
    cherv = []
    cherv.append(rec)
    count = 0
    app = 0
    siel = 0

    window.bind('<Right>', click_right)
    window.bind('<Left>', click_left)
    window.bind('<Up>', click_up)
    window.bind('<Down>', click_down)


    # btn_down =  tkinter.Button( text="D", padx="15", pady="10", command=click_down)
    # btn_up=     tkinter.Button( text="U", padx="15", pady="10", command=click_up)
    # btn_left =  tkinter.Button( text="L", padx="15", pady="10", command=click_left)
    # btn_right = tkinter.Button( text="R", padx="15", pady="10", command=click_right)
    #
    # btn_down.pack()
    # btn_up.pack()
    # btn_left.pack()
    # btn_right.pack()
    #
    # btn_down.place(x=450, y=500)
    # btn_up.place(x=450, y=400)
    # btn_left.place(x=400, y=450)
    # btn_right.place(x=500, y=450)

    window.mainloop()

window.mainloop()
