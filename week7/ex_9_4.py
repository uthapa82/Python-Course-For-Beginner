class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def read_number_served(self):
        print("the restaurant have served " + str(self.number_served) + " customers!!")

    def set_number_served(self, served_customer):
        if served_customer >= self.number_served:
            print(str(served_customer) + "customer have been served!!")
        else:
            print("sorry")
        
    def increment_number_served(self, value):
        print("A day of business")
        self.number_served += value

    def describe_restaurant(self):
        print("My restaurant name is " + self.restaurant_name.title())
        print(self.cuisine_type.title() + " is available.")
    
    def open_restaurant(self):
        print(self.restaurant_name.title()+ " is opened")

rest1 = Restaurant('burger house', 'italin dish')
print("\n")
restaurant= Restaurant('burger house', 'italin dish')
restaurant.number_served = 11
restaurant.number_served = 12
restaurant.read_number_served()

restaurant.set_number_served(22)

restaurant.increment_number_served(18)
print("\n")
rest1.describe_restaurant()
rest1.open_restaurant()