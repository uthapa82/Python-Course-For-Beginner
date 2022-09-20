def describe_city(city_name, country = 'Nepal'):
    """display information about cities and country"""
    print(city_name.title() + " is in " + country + ".")

def main():
    describe_city(city_name = 'pokhara')
    describe_city(city_name= 'NY', country= 'America')
    describe_city(city_name= 'tokyo', country = 'Japan')
    describe_city(city_name= 'delhi', country = 'India')

if __name__ == "__main__":
    main()