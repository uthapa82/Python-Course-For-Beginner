def city_country(city, country, population):
    """Return single string."""
    output = city.title() + " " + country.title()
    output += '-population ' + str(population)
    return output
    