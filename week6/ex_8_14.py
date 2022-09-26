<<<<<<< HEAD
from pyexpat import model


=======
>>>>>>> 1124fba713442250d23f88682f1ec6b862d5c059
def build_car(manufacture, model, **car_info):
    car = {
        'car name': manufacture.title(),
        'model': model.title()
    }
<<<<<<< HEAD

=======
    
>>>>>>> 1124fba713442250d23f88682f1ec6b862d5c059
    for key, value in car_info.items():
        car[key] = value
        
    return car

<<<<<<< HEAD

def main():
    car_info= build_car('subaru', 'out track', color = 'blue', two_package = True)
    print(car_info)
=======
def main():
    car_info = build_car('subaru', 'out track', color = 'blue', two_package = True)
    car_info2 = build_car('honda', 'accord', year=2014, color='blue', headlights='led')
    print(car_info)
    print(car_info2)
>>>>>>> 1124fba713442250d23f88682f1ec6b862d5c059

if __name__ == '__main__':
    main()
