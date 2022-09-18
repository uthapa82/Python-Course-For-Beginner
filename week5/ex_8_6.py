def city_country(city, country):
    """returning city and country"""
    city_country = city + " " + country
    return city_country.title()

world = city_country('"kathmandu,', 'Nepal"')
print(world)

beautiful_city = city_country('"NY,', 'america"')
print(beautiful_city)

beautiful = city_country('"pokhara,', 'nepal"')
print(beautiful)