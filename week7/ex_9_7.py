class User():
    def __init__(self, first_name, last_name, age, profession):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.age = age 
        self.profession = profession.title()
    
    def describe_user(self):
        print(self.first_name + " " + self.last_name + ", " + self.profession)

    def greet_user(self):
        print("Hello " + self.first_name + " " + self.last_name)

class Admin(User):
    def __init__(self, first_name, last_name, age, profession):
        super().__init__(first_name, last_name, age, profession)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_priviliges(self):
        for i in self.privileges:
            print(i)


user_0 = Admin('Elon', 'Musk', 38, 'CEO')
user_0.describe_user()
user_0.show_priviliges()

    