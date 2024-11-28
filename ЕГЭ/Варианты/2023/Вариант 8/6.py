from turtle import *

k = 20
screensize(2000, 2000)
tracer(0)

pendown()
right(90)
for i in range(15):
    forward(k * 5)
    left(72)

penup()
for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()