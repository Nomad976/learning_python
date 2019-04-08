vacation_spots = []

while True:
    spot = input("If you could visit one place in the world, where would you"
                 " go? ")
    if spot == 'quit':
        break
    else:
        vacation_spots.append(spot)

print("\nPoll results: ")
for spot in vacation_spots:
    print(spot)
