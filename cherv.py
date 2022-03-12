import tkinter
import time
import random

razmer_okna = 600
razmer_apple = 36
step = 3
speed = 0.01

x = random.randint(0, razmer_okna - razmer_apple)  # magic number!
y = random.randint(0, razmer_okna - razmer_apple)


def game_over():
    global razmer_okna

    citata = "Господь, как видно,\nзабирает лучших..."
    label = tkinter.Label(text=citata, fg="white", bg="black")
    label.pack()
    label.place(x=razmer_okna // 2 - 70, y=razmer_okna // 2)
    window.mainloop()


def eat():
    global x, y, x0, y0, app, apple

    if abs(x - x0) < razmer_apple and abs(y - y0) < razmer_apple:
        app += 1
        for i in range(len(cherv)):
            if abs(x - canvas.coords(cherv[i])[0]) < razmer_apple and abs(y - canvas.coords(cherv[i])[1]) < razmer_apple:
                x = random.randint(0, razmer_okna - razmer_apple)
                y = random.randint(0, razmer_okna - razmer_apple)

        canvas.delete(apple)
        apple = canvas.create_rectangle(x, y, x + razmer_apple, y + razmer_apple, fill="red")


def proverka(i):
    global rec, x0, y0
    eat()

    if (y0 + razmer_apple) > razmer_okna or (x0 + razmer_apple) > razmer_okna:
        game_over()
    if x0 < 0 or y0 < 0:
        game_over()

    if len(cherv) > razmer_apple:
        num = i - 2 * (razmer_apple // step)

        while num != (i + 1):
            if num < 0:
                num += len(cherv)

            if num == i + 1:
                break

            if (i == len(cherv) - 1) and (num == 0):
                break

            if (abs(canvas.coords(cherv[num])[0] - x0) < razmer_apple) and (abs(canvas.coords(cherv[num])[1] - y0) < razmer_apple):
                game_over()

            num -= 1
        canvas.delete(rec)
        rec = canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue")
        window.update()


def move():
    global rec, x0, y0, count, app, step, start, side
    start = 1
    while True:
        if count < app:
            for i in range(razmer_apple // step):
                cherv.append(canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue"))
                if side == 'up':
                    y0 -= step
                elif side == 'right':
                    x0 += step
                elif side == 'down':
                    y0 += step
                else:
                    x0 -= step
            count += 1

        for i in range(len(cherv)):
            canvas.delete(cherv[i])
            cherv[i] = canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue")
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
    global side, start, label
    side = 'down'
    if start == 0:
        label.destroy()
        move()


def click_up(event):
    global side, start, label
    side = 'up'
    if start == 0:
        label.destroy()
        move()


def click_left(event):
    global side, start, label
    side = 'left'
    if start == 0:
        label.destroy()
        move()


def click_right(event):
    global side, start, label
    side = 'right'
    if start == 0:
        label.destroy()
        move()


if __name__ == '__main__':
    window = tkinter.Tk()
    canvas = tkinter.Canvas(window, width=razmer_okna, height=razmer_okna)
    window.title("Червь")
    canvas.pack()

    apple = canvas.create_rectangle(x, y, x + razmer_apple, y + razmer_apple, fill="red")
    x0 = 10
    y0 = 10
    start = 0
    count = 0
    app = 0
    rec = canvas.create_rectangle(x0, y0, x0 + razmer_apple, y0 + razmer_apple, fill="blue")
    cherv = []
    cherv.append(rec)

    citata = "Вы готовы, дЕтИ?!"
    label = tkinter.Label(text=citata, fg="white", bg="black")
    label.pack()
    label.place(x=razmer_okna // 2 - 70, y=razmer_okna // 2)

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
