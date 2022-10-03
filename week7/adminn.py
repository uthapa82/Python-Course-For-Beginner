#ex_9_12.py
from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name, last_name, age, profession)
        self.privileges = []
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_priviliges(self):
        if self.privileges:
            for i in self.privileges:
                print(i)
            else:
                print("privilege is empty.")