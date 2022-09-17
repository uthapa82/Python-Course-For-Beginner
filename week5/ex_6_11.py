cities = {
    'kathmandu':  {
        'country': 'Nepal',
        'population': 200000,
        'fact': 'Mt.Everest',
        },
    'NewYok': {
        'country': 'US',
        'population': 300000,
        'fact': 'white house',
        },
    'pokhara': {
        'country': 'Nepal',
        'population': 400000,
        'fact': 'lake',
        }
}  #print the name of each city and also all information.
for city, info in cities.items():
    print("\n" + city.title() + " City:")
    #information = info['country'] + "\n" + str(info['population']) + "\n" + info['fact']
    #print(information)
    print(" It has population of " + str(info['population']))
    print(" There are many " + info['fact'])

    