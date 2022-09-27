from pyexpat import model

def build_car(manufacture, model, **car_info):
    car = {
        'car name': manufacture.title(),
        'model': model.title()
    }
    
    for key, value in car_info.items():
        car[key] = value
        
    return car

def main():
    car_info= build_car('subaru', 'out track', color = 'blue', two_package = True)
    print(car_info)

def main():
    car_info = build_car('subaru', 'out track', color = 'blue', two_package = True)
    car_info2 = build_car('honda', 'accord', year=2014, color='blue', headlights='led')
    print(car_info)
    print(car_info2)

if __name__ == '__main__':
    main()
