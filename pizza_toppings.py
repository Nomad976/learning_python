print("Please enter names of pizza toppings you would like. Enter 'quit'"
      " when you're done.")

topping = ""
while topping != 'quit':
    topping = input()
    if topping != 'quit':
        print("We'll add " + topping + " to your pizza.")
