class Dog():
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age
        
    def sit(self):
        print(self.name.title() + " is now sitting.")
        
    def roll_over(self):
        print(self.name.title() + " rolled over!") 


dog1 = Dog('Khaire', '5')
print(dog1.sit())
print(dog1.roll_over())