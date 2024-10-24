from turtle import *

k = 20
tracer(0)
screensize(2000, 2000)

pendown()
right(45)
for _ in range(9):
    forward(9 * k)
    right(90)

penup()
for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(y * k, x * k)
        dot()

done()