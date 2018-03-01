# a python script to calculate gst for pizzas

# ask the person how many pizzas they want
number_of_pizzas = input('how many pizzas would you like to order: ')

# enter the cost of the pizza, assuming the cost is all the same
cost_of_pizza = input('how much does the pizza cost :$ ')

# calculate the cost of all of the pizzas
subtotal_pizza = number_of_pizzas * cost_of_pizza

# enter the GST ammount
cost_of_GST = input('enter the GST amount in decimal eg 0.10 ')

# calculate the GST owed on all the pizzas
subtotal_GST = cost_of_GST * subtotal_pizza

# calclulate the total cost including GST
total = subtotal_pizza + subtotal_GST

#show the user the total amount due, including tax
print "The total cost is $",total
print "This includes $", subtotal_pizza, "for the Pizza and"
print "$", subtotal_GST, "in GST"

