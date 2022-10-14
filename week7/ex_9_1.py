class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print("My resturant name is " + self.resturant_name.title())
        print(self.cuisine_type.title() + " is available.")
    
    def open_resturant(self):
        print(self.resturant_name.title()+ " is opened")

rest1 = Resturant('burger house', 'italin dish')

rest1.describe_resturant()
rest1.open_resturant()