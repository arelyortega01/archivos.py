#arely ortega quiroz 

from turtle import *
from colorsys import *

bgcolor("black")
speed(0)
pensize(3)

h = 0

def color_random():
    global h
    color(hsv_to_rgb(h, 1, 1))
    h += 0.02

def linea(x1, y1, x2, y2):
    penup()
    goto(x1, y1)
    pendown()
    goto(x2, y2)

# A
color_random()
linea(-300, -100, -275, 100)
linea(-250, -100, -275, 100)
linea(-290, 0, -260, 0)

# R
color_random()
linea(-220, 100, -220, -100)
linea(-220, 100, -170, 100)
linea(-220, 0, -170, 0)
linea(-170, 100, -170, 0)
linea(-220, 0, -170, -100)

# E
color_random()
linea(-140, 100, -140, -100)
linea(-140, 100, -90, 100)
linea(-140, 0, -100, 0)
linea(-140, -100, -90, -100)

# L
color_random()
linea(-60, 100, -60, -100)
linea(-60, -100, -10, -100)

# Y
color_random()
linea(20, 100, 45, 0)
linea(70, 100, 45, 0)
linea(45, 0, 45, -100)

hideturtle()
done()
