sandwich_orders = ['tuna', 'pastrami', 'pastrami', 'pepperoni', 'cheese',
                   'pastrami']
finished_sandwiches = []

print("The Deli has run out of pastrami.\n")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print("I made a " + sandwich + " sandwich.")
    finished_sandwiches.append(sandwich)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich + " sandwich")
