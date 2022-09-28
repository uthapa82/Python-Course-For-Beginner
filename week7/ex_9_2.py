class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print("My resturant name is " + self.resturant_name.title())
        print(self.cuisine_type.title() + " is available.")
    
    def open_resturant(self):
        print(self.resturant_name.title()+ " is opened")

resturant = Resturant('burger house', 'italin dish')

resturant1 = Resturant('chineese resturant', 'chineese dish')
resturant2 = Resturant('Nepalese resturant', 'neplease dish')
resturant3 = Resturant('indian resturant', 'indian dish')

resturant.describe_resturant()
resturant1.describe_resturant()
resturant2.describe_resturant()
resturant3.describe_resturant()

resturant.open_resturant()