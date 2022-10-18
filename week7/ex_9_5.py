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
        print("Hello " + self.first_name + " " + self.last_name)

user_0 = User('abhi', 'lamichhane', 15, 'student')
user1 = User('anup', 'thapa', 22, 'business man')

user_0.describe_user()
user1.describe_user()
user1.greet_user()

user_2 = User('abhi', 'lamichhane', 15, 'student')
user_2.increment_login_attempts()
user_2.increment_login_attempts()
user_2.increment_login_attempts()
print(user_2.login_attempts)

user_2.reset_login_attempts()
print(user_0.login_attempts)