cities_0 = {
    'kathmandu':  {'country': 'it is inNepal', 
                 'population': ' with 20M popu.', 
                 'fact': 'fact is fact',},
    'NewYok': {'country': 'is in US', 
               'population': ' ith 30Mpopu.', 
               'fact': 'not in US',},
    'pokhara': {'country': 'is in Nepal', 
                'population': ' with 40M popu.',
                'fact': 'fact',}
}  #print the name of each city and also all information.
for city, info in cities_0.items():
    print("\n" + city.title() + " City:")
    information = info['country'] + info['population'] + "\n" + info['fact']
    print(information)

    