

# SquareSpiral1.py - Draws a square spiral
import turtle
t = turtle.Pen()
colors = ['red', 'blue']
for x in range(900):
	t.pencolor(colors[x%2])	
	t.forward(x)
	t.right(90)
