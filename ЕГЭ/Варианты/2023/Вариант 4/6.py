from turtle import *

k = 20
tracer(0)
screensize(2000, 2000)

pendown()
color("red")
forward(200 * k)
setpos(0, 0)
backward(2 * 200 * k)
setpos(0, 0)
right(90)

x = 1
total = 19 + 10 * x
while total < 25000:
    print(total, x)
    total = 19 + 10 * x
    x += 1

color("black")
forward(2 * k)
for i in range(5):
    forward(x * k)
    right(90)
    forward(3 * k)
    right(90)
    forward(x * k)
    left(90)
    forward(1 * k)
    left(90)   
backward(2 * k)
penup()

for y in range(-20, 20):
    for x in range(-20, 20):
        setpos(x * k, y * k)
        dot()

done()