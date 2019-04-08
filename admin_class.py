from user_class import User


class Privileges:
    """This class contains privileges of the admin."""

    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        """Show admin's privileges."""
        print("\nAdmin's privileges: ")
        for privilege in self.privileges:
            print(privilege)


class Admin(User):
    """This class contains an admin profile."""

    def __init__(self, first, last, passed_age):
        super().__init__(first, last, passed_age)
        self.admin_privileges = Privileges()
