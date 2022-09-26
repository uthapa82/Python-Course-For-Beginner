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

if __name__ == '__main__':
    main()
