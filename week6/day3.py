import build_car as b
import math as m


def math_eg():
    result = m.remainder(9, 2)
    return result

def main():
    car_info = b.build_car('subaru', 'out track', color = 'blue', two_package = True)
    car_info2 = b.build_car('honda', 'accord', year=2014, color='blue', headlights='led')
    print(car_info)
    print(car_info2)
    print(math_eg())

if __name__ == '__main__':
    main()