class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("My restaurant name is " + self.restaurant_name.title())
        print(self.cuisine_type.title() + " is available.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title()+ " is opened")
