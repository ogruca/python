#Circel Spiral.
import turtle
t = turtle.Pen()
colors = ['red', 'blue']
for x in range(900):
        t.pencolor(colors[x%2])
        t.circle(x)
        t.right(91)

