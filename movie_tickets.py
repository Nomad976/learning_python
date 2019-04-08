print("Enter your age and we'll inform you how much your ticket costs.")
input_age = ""
while input_age != 'quit':
    input_age = input()
    if input_age == 'quit':
        break
    else:
        age = int(input_age)
        if age > 12:
            print("Your ticket costs $15.")
        elif age > 3:
            print("Your ticket costs $10.")
        else:
            print("Your ticket is free.")
