#SquareSpiral2.py - Draws a square spiral shifted by 91 degrees
import turtle
t = turtle.Pen()
colors = ['black', 'pink']
for x in range(900):
        t.pencolor(colors[x%2])
        t.forward(x)
        t.right(91)

