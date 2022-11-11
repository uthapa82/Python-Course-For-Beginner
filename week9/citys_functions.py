def city_country(city, country, population=0):
    """Return string"""
    output = city.title() + " " + country.title()
    if population:
        output += '-population' + str(population)
    return output
