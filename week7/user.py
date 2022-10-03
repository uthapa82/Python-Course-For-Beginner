#ex_9_12
class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
        self.login_attempts = 0

    def increment_login_attempts(self):
        print("you have login " + str(self.login_attempts) + " times")
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts == 0
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is a " + self.profession)

    def greet_user(self):
        print("Hello " + self.first_name + "  " + self.last_name)