from turtle import *
import time

screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
#
canvas = screen.getcanvas()
root = canvas.winfo_toplevel().attributes('-fullscreen', True)

screen.update()
time.sleep(1)

t = Turtle()
t.speed(0)
t.width(3)

colors = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#ae0d8b", "#8B00FF"]

for i in range(800):
    t.color(colors[i % len(colors)])
    t.circle(20 + i, 60)
    t.left(59)
    for j in range(3): 
        t.forward(i * 1.2)
        t.right(120)

    if i < 100:
        screen.update()
    elif 200 > i > 100 and i % 2 == 0:
        screen.update()
    elif 300 > i > 200 and i % 3 == 0:
        screen.update()
    elif 400 > i > 300 and i % 4 == 0:
        screen.update()
    elif 500 > i > 400 and i % 5 == 0:
        screen.update()
    elif 600 > i > 500 and i % 6 == 0:
        screen.update()
    elif 700 > i > 600 and i % 8 == 0:
        screen.update()
    elif 800 > i > 700 and i % 10 == 0:
        screen.update()

exitonclick()
screen.mainloop()