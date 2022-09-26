def build_car(manufacture, model, **car_info):
    car = {
        'car name': manufacture.title(),
        'model': model.title()
    }
    
    for key, value in car_info.items():
        car[key] = value
        
    return car