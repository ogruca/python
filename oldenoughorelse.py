driving_age = eval(raw_input("What is the legal driving age where you live?: "))
your_age = eval(raw_input("How old are you?:  "))
if your_age >= driving_age:
	print("You are old enough to drive!!!")
else:
	print("Sorry, you can drive in", driving_age - your_age, "years")