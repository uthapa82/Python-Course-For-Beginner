class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print("My resturant name is " + self.resturant_name.title())
        print(self.cuisine_type.title() + " is available.")
    
    def open_resturant(self):
        print(self.resturant_name.title()+ " is opened")

class IceCreamStand(Resturant):
    def __init__ (self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = []

    def display_flavor(self):
        self.flavor = ["strawberry", "vanela"]
        print("This resturant have " + str(self.flavor) + " flavor ice cream")

flavor_0 = IceCreamStand('WilliFood', 'italian',)
flavor_0.display_flavor()

#flavor_0.display_flavor()

