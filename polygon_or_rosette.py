import turtle
t = turtle.Pen()
#Ask the user fo the number of sides or circles, default to 6
number = int(turtle.numinput("Number of sides or circles", "How many side or circles in your shape?", 6))
#Ask the user whether they want a polygoon or rosette
shape = turtle.textinput("Which shape do you want?", "Enter 'p' for polygon or 'r' for rosette:")
for x in range(number):
	if shape == 'r':	#user selected rosette
		t.circle(100)
	else:				#default to polygon
		t.forward(150)
	t.left(360/number)
