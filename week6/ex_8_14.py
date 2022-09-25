from pyexpat import model


def build_car(manufacture, model_name, **car_info):
    car = {}
    car['car_name'] = manufacture
    car['model'] = model_name

    for key, value in car_info.items():
        car[key] = value
    return car

car_info = build_car('subaru', 'out track', color = 'blue', two_package = True)

print(car_info)

