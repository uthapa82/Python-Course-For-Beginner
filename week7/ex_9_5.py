class User():
    def __init__(self, first_name, last_name, age, profession, login_attempts):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
        self.login_attempts = login_attempts

    def increment_login_attempts(self, value):
        print("you have login " + str(self.login_attempts) + " times")
        self.login_attempts += value
        
    def reset_login_attempts(self, reset_login):
        if reset_login == 0:
            print("you have successfull reset you login")
            self.login_attempts = reset_login
        else:
            print("please reset your login")
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + " is a " + self.profession)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

user = User('abhi', 'lamichhane', 15, 'student', 0)
user1 = User('anup', 'thapa', 22, 'business man', 0)

user.describe_user()
user1.describe_user()
user1.greet_user()

user_2 = User('abhi', 'lamichhane', 15, 'student', 0)
user_2.increment_login_attempts(1)
user_2.increment_login_attempts(3)
user_2.increment_login_attempts(2)
print(user_2.login_attempts)

user_2.reset_login_attempts(0)
user_2.reset_login_attempts(1)
print(user_2.login_attempts)