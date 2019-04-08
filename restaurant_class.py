class Restaurant:
    """Model a restaurant."""

    def __init__(self, name, cuisine):
        """Initialise restaurant_name nad cuisine_type attributes."""
        self.restaurant_name = name
        self.cuisine_type = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """Print all the information about a restaurant."""
        print("This restaurant is called " + self.restaurant_name.title() +
              " and serves " + self.cuisine_type.title() + " cuisine.")

    def open_restaurant(self):
        """Open a restaurant."""
        print(self.restaurant_name.title() + " is open.")

    def set_number_served(self, number):
        """Set the number of served customers."""
        self.number_served = number

    def increment_number_served(self, number):
        """Increment the number of served customers by a given number."""
        self.number_served += number
