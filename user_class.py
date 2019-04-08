class User:
    """This class contains a user profile."""

    def __init__(self, first, last, passed_age):
        self.first_name = first
        self.last_name = last
        self.age = passed_age
        self.login_attempts = 0

    def describe_user(self):
        print("\nFirst name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Age: " + str(self.age))
        print("Login attempts: " + str(self.login_attempts))

    def greet_user(self):
        print("\nHello " + self.first_name.title() + " " +
              self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

