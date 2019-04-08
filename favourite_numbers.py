favourite_numbers = {
    'jen': [7],
    'chris': [9, 3],
    'alice': [13],
    'emily': [21, 1000, 37, 57],
    'frank': [500, 1, 2],
    }

for name, numbers in favourite_numbers.items():
    print(name.title() + "'s favourite numbers are:")
    for number in numbers:
        print(number)
