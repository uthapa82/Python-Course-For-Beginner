import build_bikes as a

def main():
    bike_info = a.build_bikes('honda', 'out track', color = 'red', CC = 500)
    bike_info2 = a.build_bikes('bullet', 2019, color = 'black', cc = 800)
    print(bike_info)
    print(bike_info2)

if __name__ == '__main__':
    main()

