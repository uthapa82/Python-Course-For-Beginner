class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + ", " + self.profession)
        print("  Username: " + self.first_name + " " + self.last_name)
        print("  Age: " + str(self.age))
        print("  Profession: " + self.profession)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

    def increment_login_attempts(self):
        print("you have login " + str(self.login_attempts) + " times")
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts == 0

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