def build_bikes(manufacture, model, **bike_info):
    bikes = {
        'bike name': manufacture.title,
        'model': model.title,
    }
    for key, value in bike_info.items():
        bikes[key] = value

    return bikes

