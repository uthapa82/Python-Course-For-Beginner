class Car():

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        print("this car has " + str(self.odometer_reading) + " miles on it.")

    def upadate_odometer(self, mileage):
        if mileage >= self.odometer_ready:
            self.odometer_reading = mileage
        else:
            print("yu can't roll back an odometer.")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery():
    def __init__(self, battery_size = 60):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + ("-KWH battery"))

    def get_range(self):
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range == 190
        
        message = "This car can go approximately " + str(range)
        message += "miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size == 60:
            self.battery_size = 85
            print("battery upgraded to 85")
        else:
            print("battery upgraded")

class ElectricCar(Car):
    def __init__(self, manufacture, model, year):
        super().__init__(manufacture, model, year)
        self.battery = Battery()

my_car = ElectricCar('Toyota', 'corolla', 2019)
my_car.battery.describe_battery()
my_car.battery.upgrade_battery()