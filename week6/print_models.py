def build_bikes(manufacture, model, **bike_info):
    bikes = {
        'bike name': manufacture.title,
        'model': model.title,
    }
    for key, value in bike_info.items():
        bikes[key] = value

    return bikes

def main():
     bike_info = build_bikes('honda', 'out track', color = 'red', CC = 500)
     print(bike_info)

if __name__ == '__main__':
    main()