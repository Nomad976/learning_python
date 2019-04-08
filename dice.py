from random import randint


class Die:
    """A simple attempt in describing a rolling die."""

    def __init__(self, passed_sides=6):
        self.sides = passed_sides

    def roll_die(self):
        """Roll die."""
        random = randint(1, self.sides)
        print("\nRolled: " + str(random))
        print("Number of sides: " + str(self.sides))


my_die = Die(20)
for val in range(0, 10):
    my_die.roll_die()
