pizzas = ['margherita', 'vesuvio', 'feliciana']
for pizza in pizzas:
    print("I like " + pizza + " pizza.")
print("\nI like pizza.")

friend_pizzas = pizzas[:]
pizzas.append('guseppe')
friend_pizzas.append('roma')

print("\nMy favourite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's' favourite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
