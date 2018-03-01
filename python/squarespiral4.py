#SquareSpiral2.py - Draws a square spiral
import turtle
t = turtle.Pen()
sides = input("Enter a number of sides between 2 and 6: ")
colors = ['red', 'blue', 'orange', 'green', 'yellow', 'purple']
for x in range(900):
        t.pencolor(colors[x%sides])
        t.forward(x * 3/sides + x)
        t.right(360/sides + 1)
	t.width(x*sides/200)
